
import React, { useEffect, useState } from 'react'

import axios from 'axios'

function Csv_test() {
  const [data ,setData]=useState(null)
  const apiCall=async()=>{
      let fom_data=new FormData()
      fom_data.append('file', data)
      let res=await axios.post("http://127.0.0.1:5000/download_the_predicts_file", fom_data , {headers: {
          'Content-Type': 'multipart/form-data',
        }, responseType:'blob'})
    return res
  }
  
  const handle_submit_button=async(e)=>{
    e.preventDefault()
    if(data==null){
        alert('please upload the test csv file')
    }
    let data1=await apiCall()
    if(data1.status==200){
        window.location.href="http://127.0.0.1:5000/download_pred_file"
    }

  }
  return (
  <div className="flex items-center justify-center min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
  <div className="bg-black p-8 rounded-3xl shadow-xl w-full max-w-md border border-gray-100">
    
    <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">
      Upload Your CSV
    </h2>
    
    <div className="mb-6">
      <label className="block text-sm font-medium text-gray-600 mb-2">
        Select CSV File
      </label>
      <input 
        type="file" 
        accept=".csv"
        onChange={(e) => setData(e.target.files[0])} 
        className="block w-full text-sm text-gray-700 border border-gray-300 rounded-xl cursor-pointer file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-medium file:bg-blue-50 file:text-blue-600 hover:file:bg-blue-100 focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
    </div>
    
    <button 
      onClick={handle_submit_button}
      className="w-full bg-blue-600 text-white py-3 rounded-xl font-medium text-lg shadow-md hover:bg-blue-700 hover:shadow-lg transition-all duration-300"
    >
      Test the Data
    </button>
  
  </div>
</div>


  )
}

export default Csv_test

