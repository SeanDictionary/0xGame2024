import "@/styles/globals.css";
import Head from 'next/head'

export default function App({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>Next.db</title>
      </Head>
      <Component {...pageProps} />
    </>
  );
}
