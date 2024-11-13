import { useState } from "react";
import localFont from "next/font/local";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export default function Home() {
  const [name, setName] = useState("");
  const [data, setData] = useState([]);
  const [showTable, setShowTable] = useState(false); // 控制表格显示状态
  const [errorMessage, setErrorMessage] = useState(""); // 存储错误消息

  const handleSearch = async () => {
    if (!name.trim()) return;

    try {
      const res = await fetch("/api/search", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name }),
      });

      if (!res.ok) {
        const errorData = await res.json(); // 获取返回的错误 JSON 数据
        setErrorMessage(errorData.message);
        return;
      }

      const result = await res.json();

      setData(result);
      setShowTable(true); // 搜索后显示表格
    } catch (error) {
      setErrorMessage("Network error, please try again later.");
    }
  };

  return (
    <div
      className={`${geistSans.variable} ${geistMono.variable} grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]`}
    >
      <main className="flex flex-col gap-8 row-start-2 items-center">

        <h1 className="text-2xl sm:text-4xl font-bold text-center font-[family-name:var(--font-geist-mono)]">
          Next.
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-blue-500 to-purple-500">
            db
          </span>
        </h1>

        <div className="relative flex gap-2 items-center">
          <input
            type="text"
            placeholder="Search by name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            className="w-64 h-12 border border-gray-300 rounded-full px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={handleSearch}
            className="h-12 rounded-full border border-solid border-transparent transition-colors flex items-center justify-center bg-foreground text-background gap-2 hover:bg-[#383838] dark:hover:bg-[#ccc] text-sm sm:text-base px-4 sm:px-5"
          >
            Search
          </button>
        </div>

        {/* 提示框 */}
        {errorMessage && (
          <div className="bg-red-500 text-white px-4 py-2 rounded-lg shadow-lg">
            <p>{errorMessage}</p>
            <button onClick={() => setErrorMessage("")} className="mt-2 text-sm underline">
              Close
            </button>
          </div>
        )}

        {/* 表格区域 - 使用渐变加速动画 */}
        <div
          className={`w-full max-w-4xl overflow-hidden transition-all duration-700 ease-in-out ${showTable ? "max-h-[500px] opacity-100" : "max-h-0 opacity-0"
            }`}
          style={{
            transitionTimingFunction: "cubic-bezier(0.4, 0, 0.2, 1)", // 自定义贝塞尔曲线
          }}
        >
          <div className="flex flex-col">
            <div className="-m-1.5 overflow-x-auto">
              <div className="p-1.5 min-w-full inline-block align-middle">
                <div className="overflow-hidden">
                  <table className="min-w-full divide-y divide-gray-200">
                    <thead>
                      <tr>
                        <th
                          scope="col"
                          className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                        >
                          ID
                        </th>
                        <th
                          scope="col"
                          className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                        >
                          Name
                        </th>
                        <th
                          scope="col"
                          className="px-6 py-3 text-start text-xs font-medium text-gray-500 uppercase"
                        >
                          Description
                        </th>
                      </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-200">
                      {data.length > 0 ? (
                        data.map((item) => (
                          <tr key={item.id}>
                            <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800">
                              {item.id}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                              {item.name}
                            </td>
                            <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-800">
                              {item.description}
                            </td>
                          </tr>
                        ))
                      ) : (
                        <tr>
                          <td
                            colSpan="3"
                            className="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-800"
                          >
                            No results found.
                          </td>
                        </tr>
                      )}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>

      <footer className="row-start-3 flex gap-6 flex-wrap items-center justify-center">
        <a className="hover:underline hover:underline-offset-4" target="_blank" href="https://nextjs.org/">
          Built with Next.js
        </a>
      </footer>
    </div>
  );
}
