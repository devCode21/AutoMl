import React, { useState } from 'react';
import axios from 'axios';

function Csv_test() {
  const [data, setData] = useState(null);
  const [isUploading, setIsUploading] = useState(false);

  const apiCall = async () => {
    let fom_data = new FormData();
    fom_data.append('file', data);
    let res = await axios.post("http://127.0.0.1:5000/download_the_predicts_file", fom_data, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return res;
  };

  const handle_submit_button = async (e) => {
    e.preventDefault();
    if (data === null) {
      alert('Please upload a CSV file.');
      return;
    }

    setIsUploading(true);
    try {
      const response = await apiCall();
      if (response.status === 200) {
        window.location.href = "http://127.0.0.1:5000/download_pred_file";
        alert('File processed successfully! Downloading now...');
      }
    } catch (error) {
      console.error('Error during file processing:', error);
      alert('An error occurred. Please try again.');
    } finally {
      setIsUploading(false);
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-100 p-4">
      <div className="bg-white p-8 rounded-2xl shadow-lg w-full max-w-sm text-center transform hover:scale-105 transition-transform duration-300">
        <h2 className="text-3xl font-bold text-gray-800 mb-4">
          Test Your Data
        </h2>
        <p className="text-gray-500 mb-6">
          Upload a CSV file to get predictions.
        </p>

        <div className="mb-6">
          <label className="flex flex-col items-center justify-center w-full h-40 border-2 border-dashed border-gray-300 rounded-xl cursor-pointer bg-gray-50 hover:bg-gray-100 transition-colors duration-200">
            <svg
              className="w-12 h-12 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v8"
              ></path>
            </svg>
            <p className="text-sm text-gray-500 mt-2">
              <span className="font-semibold">Click to upload</span> or drag and drop
            </p>
            <p className="text-xs text-gray-500 mt-1">
              {data ? data.name : 'CSV only (MAX. 5MB)'}
            </p>
            <input
              type="file"
              accept=".csv"
              onChange={(e) => setData(e.target.files[0])}
              className="hidden"
            />
          </label>
        </div>

        <button
          onClick={handle_submit_button}
          disabled={isUploading || !data}
          className={`w-full py-3 rounded-lg font-semibold text-lg transition-colors duration-300 ${
            isUploading || !data
              ? 'bg-blue-300 text-white cursor-not-allowed'
              : 'bg-blue-600 text-white hover:bg-blue-700'
          }`}
        >
          {isUploading ? 'Processing...' : 'Test the Data'}
        </button>
      </div>
    </div>
  );
}

export default Csv_test;