import React, { useEffect } from "react";
import { ArrowRight, Cpu, FileUp, GanttChart, Download } from "lucide-react";

function HomePage() {
  useEffect(() => {
    localStorage.clear();
  }, []);

  return (
    <div className="min-h-screen flex flex-col bg-slate-950 text-slate-100 font-sans antialiased">
      {/* Header */}
      <header className="flex justify-between items-center px-4 sm:px-10 py-6 border-b border-slate-800">
        <div className="flex items-center space-x-2">
          <Cpu className="h-6 w-6 text-emerald-400" />
          <h1 className="text-xl font-bold tracking-tight text-slate-100">
            AutoML Studio
          </h1>
        </div>
        <nav className="hidden md:flex space-x-6 text-sm text-slate-400 font-medium">
          <a href="/train" className="hover:text-emerald-400 transition-colors">
            Train
          </a>
          <a href="#" className="hover:text-emerald-400 transition-colors">
            Test
          </a>
          <a href="#" className="hover:text-emerald-400 transition-colors">
            Report
          </a>
        </nav>
      </header>

      {/* Hero Section */}
      <main className="flex-grow flex flex-col items-center justify-center text-center p-6 sm:p-10">
        <div className="max-w-3xl">
          <h2 className="text-4xl sm:text-5xl font-extrabold text-slate-50 leading-tight mb-4">
            Automate Your Machine Learning Journey
          </h2>
          <p className="text-lg text-slate-400 leading-relaxed mb-8">
            Upload your dataset, preprocess automatically, build models, and get
            predictions — all in one streamlined workflow. Currently supporting
            supervised learning (classification & regression).
          </p>
          <a
            href="/train"
            className="inline-flex items-center px-8 py-4 bg-emerald-600 hover:bg-emerald-700 rounded-xl text-lg font-semibold transition-transform transform hover:scale-105 shadow-lg"
          >
            <Cpu size={20} className="mr-3" />
            Start Training
            <ArrowRight size={18} className="ml-3" />
          </a>
        </div>
      </main>

      {/* Features Section */}
      <section className="bg-slate-900 py-16">
        <div className="container mx-auto px-4">
          <h2 className="text-3xl font-bold text-center mb-12 text-slate-50">
            Key Features
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            <div className="p-8 bg-slate-800 rounded-2xl shadow-lg border border-slate-700 hover:border-emerald-400 transition-all duration-300">
              <div className="flex items-center justify-center w-14 h-14 bg-emerald-500 rounded-full mb-4">
                <FileUp className="text-slate-900 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold mb-2 text-slate-50">
                Data Preprocessing
              </h3>
              <p className="text-slate-400">
                Handle missing values, outliers, encoding, and scaling
                automatically with zero effort.
              </p>
            </div>
            <div className="p-8 bg-slate-800 rounded-2xl shadow-lg border border-slate-700 hover:border-emerald-400 transition-all duration-300">
              <div className="flex items-center justify-center w-14 h-14 bg-emerald-500 rounded-full mb-4">
                <GanttChart className="text-slate-900 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold mb-2 text-slate-50">
                Model Selection & Tuning
              </h3>
              <p className="text-slate-400">
                Train multiple models and pick the best one using accuracy or R²
                score — auto tuned for you.
              </p>
            </div>
            <div className="p-8 bg-slate-800 rounded-2xl shadow-lg border border-slate-700 hover:border-emerald-400 transition-all duration-300">
              <div className="flex items-center justify-center w-14 h-14 bg-emerald-500 rounded-full mb-4">
                <Download className="text-slate-900 w-8 h-8" />
              </div>
              <h3 className="text-xl font-semibold mb-2 text-slate-50">
                Export & Predict
              </h3>
              <p className="text-slate-400">
                Download reports, transformed datasets, and ready-to-use
                prediction files instantly.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 text-center text-sm text-slate-500 border-t border-slate-800">
        © {new Date().getFullYear()} AutoML Studio · Simplifying ML for Everyone
      </footer>
    </div>
  );
}

export default HomePage;