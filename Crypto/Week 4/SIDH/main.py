from server import *
from random import randint
from secret import flag

class test(Task):
    def handle(self):
        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.alarm(300)
        ea, eb = 110, 67
        p = 2**ea*3**eb - 1
        F.<i> = GF(p**2, modulus=[1,0,1])

        E0 = EllipticCurve(F, [1,0])

        PA = E0.random_point()
        QA = E0.random_point()
        sA = randint(0, 2**ea)
        RA = PA + sA*QA
        self.send((f'[+] RA = {RA.xy()}').encode())
        self.send((f'[+] Give me RB:').encode())
        RB_= [int(i) for i in self.recv().decode().split(',')]
        #Example: 1,2,3,4 

        RB = E0(RB_[0]*i + RB_[1], RB_[2]*i + RB_[3])
        phi_B =  E0.isogeny(RB, algorithm='factored')
        E_B = phi_B.codomain()
        assert E_B.is_isogenous(E0)

        R_share = phi_B(PA) + sA * phi_B(QA)
        phi_share = E_B.isogeny(R_share, algorithm='factored')
        secret = phi_share.codomain().j_invariant()
        self.send(b'[+] Tell me the secret')
        secret_ = [int(i) for i in self.recv().decode().split(',')]
        secret_ = secret_[0] * i + secret_[1]

        if secret_ == secret:
            self.send((f'[+] flag:{flag}').encode())
        else:
            self.send(b'[!] Wrong')


if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10012
    server = ForkedServer((HOST, PORT), test)
    server.allow_reuse_address = True
    print(HOST, PORT)
    server.serve_forever()