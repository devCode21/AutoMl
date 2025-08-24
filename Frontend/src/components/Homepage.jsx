import React from "react";

function HomePage() {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      {/* Header */}
      <header className="bg-white shadow-sm py-4 px-8 flex justify-between items-center">
        <h1 className="text-2xl font-bold text-blue-700">AutoML Studio</h1>
        <nav className="space-x-8 text-gray-600 font-medium">
          <a href="/train" className="hover:text-blue-600">Home</a>
          <a href="#" className="hover:text-blue-600">Train</a>
          <a href="#" className="hover:text-blue-600">Test</a>
          <a href="#" className="hover:text-blue-600">Report</a>
        </nav>
      </header>

      {/* Hero Section */}
      <main className="flex-grow flex flex-col justify-center items-center text-center px-6">
       

        {/* Single Action Card */}
        <div className="bg-white p-10 rounded-2xl shadow-md hover:shadow-lg transition text-center max-w-md w-full">
          <h3 className="text-xl font-semibold mb-3 text-blue-700">⚡ Train Models</h3>
          <p className="text-gray-600 mb-6">
            Start building supervised learning models instantly with automated workflows.
          </p>
          <button className="px-8 py-3 rounded-xl bg-blue-600 text-white font-medium hover:bg-blue-700 transition text-lg">
            <a href="/train">Start Training</a>
          </button>
        </div>
      </main>

      {/* Footer */}
      <footer className="bg-gray-100 py-4 text-center text-gray-500 text-sm">
        © {new Date().getFullYear()} AutoML Studio · Train Models Effortlessly
      </footer>
    </div>
  );
}

export default HomePage;
