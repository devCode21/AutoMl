import React, { useEffect, useState } from "react";
import axios from "axios"
import { useNavigate } from "react-router";

async function model_file(){
        const res=await axios.get("")
}



function x_tarnsformed(){
    

}

function Report({api}) {
  const [trained, setTrained] = useState("");
  const [Report_data, setReportData] = useState({});
  const [upload_csv ,set_upload_csv]=useState(false)
  const [form ,set_form]=useState(false)
  const navigate=useNavigate()
  useEffect(() => {
  const id = setInterval(async () => {
    let res = await axios.get("http://127.0.0.1:5000/metrics");
    if (res.status === 200) {
      setReportData(res.data);
      clearInterval(id); // stop once success
    }
  }, 7000);

  // cleanup if component is removed
  return () => clearInterval(id);
 }, []);


  const model_download=async(e)=>{
        e.preventDefault()
        console.log("clicked")
        window.location.href = "http://127.0.0.1:5000/download_the_tuned_model";
    }
  
 
   


    
   
  const handle_train_button=(e)=>{
     e.preventDefault()
        if(upload_csv==true){
          console.log("building")
        }
        else if(form==true){
          navigate('/test_form_data')
        }
      else{
        console.log("enter type of data you want to train")
      }
   }

  
  
  return (
    <div className="Report m-8 p-6 bg-white rounded-2xl shadow-lg border border-gray-200 space-y-6">
      {/* Report Data Section */}
      <div className="space-y-2">
        <h2 className="text-xl font-semibold text-gray-800 border-b pb-2">
          Report Data
        </h2>
        {Report_data && Object.keys(Report_data).length > 0 ? (
          Object.keys(Report_data).map((val, index) => (
            <div
              key={index}
              className="flex justify-between bg-gray-50 px-4 py-2 rounded-lg text-gray-700"
            >
              <span className="font-medium">{val}</span>
              <span>{Report_data[val]}</span>
            </div>
          ))
        ) : (
          <p className="text-gray-500 italic">Report data fetching......</p>
        )}
      </div>

      {/* Downloads */}
      {api==1 &&
        <div className="h-40 flex-col">
         <div className="dwnload flex flex-col md:flex-row justify-between gap-4 mb-5">
        <button  onClick={model_download} className="px-5 py-2 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition">
          Download Model
        </button>
        <button className="px-5 py-2 rounded-lg bg-green-600 text-white font-medium hover:bg-green-700 transition">
          Check Transformed Data (CSV)
        </button>
        <button className="px-5 py-2 rounded-lg bg-purple-600 text-white font-medium hover:bg-purple-700 transition">
          Download X_transformed
        </button>
      </div>
      <div className="train_model flex flex-col md:flex-row items-center justify-between gap-6 p-4 border rounded-xl bg-gray-50">
        <label className="flex items-center gap-2 text-gray-700">
          <input type="checkbox" checked={upload_csv}  onChange={(e)=>{set_upload_csv(e.target.checked) ,set_form(false)}}   className="w-4 h-4 accent-blue-600" />
          Upload Test File (CSV)
        </label>
        <label className="flex items-center gap-2 text-gray-700">
          <input type="checkbox"  checked={form}  onChange={(e)=>{(set_form(e.target.checked) ,set_upload_csv(false)) }} className="w-4 h-4 accent-green-600" />
          Form Features
        </label>
        <button onClick={handle_train_button} className="px-6 py-2 rounded-lg bg-indigo-600 text-white font-medium hover:bg-indigo-700 transition">
          Train Model
        </button>
      </div>
        
        </div>
    }
      
    </div>
  );
}

export default Report;
