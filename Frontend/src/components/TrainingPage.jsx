import React, { useEffect, useState } from "react";
import axios from 'axios';
import { useNavigate } from "react-router";
import Report from "./report";

async function call_api(data,targetCol ,typeOfModel){
  
    const formData = new FormData();
    formData.append('file', data)
    let result=await axios.post(`http://127.0.0.1:5000/Predict_csv_file/${targetCol}/${typeOfModel}`,formData,{
        headers: {
          'Content-Type': 'multipart/form-data',
        }})
    return result
}

function TrainingPage() {
  const [chnage ,setchange]=useState(0)
  const [dataset, setDataset] = useState(null);
  const [targetCol, setTargetCol] = useState("");
  const [typeOfModel, setTypeOfModel] = useState("");
  const [api ,setapi]=useState("0")

  const nav=useNavigate()

  useEffect(()=>{
       let api1=async()=>{
            if(dataset || targetCol!="" ||typeOfModel!=""){
            let val=await call_api(dataset,targetCol,typeOfModel)
            if(val.status==200){
              setapi(1)
              console.log(api)
            }
       }
       }
       api1()
       
  },[chnage])
  
  const handleSubmit= (e)=>{
    e.preventDefault()
    if(!dataset || targetCol=="" ||typeOfModel==""){
      console.log("enter all details")
      return
    }
   
  
    setchange(1)
    console.log(typeOfModel)
   
   
    
    
    
  }


  return (
    <>
         {chnage===0?<div  className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-100 via-white to-gray-200 p-6">
      <div className="w-full max-w-lg bg-white rounded-2xl shadow-xl border border-gray-200 p-8">
        <h1 className="text-2xl font-bold text-gray-800 text-center mb-6">
          Train Your Dataset
        </h1>

        <form className="space-y-6" onSubmit={handleSubmit}>
          {/* Upload Dataset */}
          <div className="flex flex-col space-y-2">
            <label htmlFor="Data" className="text-sm font-medium text-gray-700">
              Upload Dataset
            </label>
            <input
              type="file"
              id="Data"
              className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
              onChange={(e) => setDataset(e.target.files[0])}
            />
          </div>

          {/* Target Column */}
          <div className="flex flex-col space-y-2">
            <label
              htmlFor="Target"
              className="text-sm font-medium text-gray-700"
            >
              Target Column
            </label>
            <input
              type="text"
              id="Target"
              placeholder="Enter target column"
              value={targetCol}
              onChange={(e) => setTargetCol(e.target.value)}
              className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
            />
          </div>

          {/* Select Type */}
          <div className="flex flex-col space-y-2">
            <label className="text-sm font-medium text-gray-700">
              Choose Type of Model
            </label>
            <select
              value={typeOfModel}
              onChange={(e) => setTypeOfModel(e.target.value)}
              className="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-400"
            >
              <option value="" disabled>
                Select type
              </option>
              <option value="classification">Classification</option>
              <option value="Regressor">Regressor</option>
            </select>
          </div>

          {/* Submit Button */}
          <div className="flex justify-center">
            <button
              type="submit"
              className="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-medium py-2 px-4 rounded-lg shadow-md transition duration-200"
            >
              Train the Dataset
            </button>
          </div>
        </form>
      </div>
    </div>:<>{<Report api={api}/>}</>}
    </>
   
  );
}

export default TrainingPage;

// message ayega ok uske badd redirect to next page where i would give 3 option download pkl ,test_model model and report of the model right