import axios from "axios";
import React, { useState, useEffect } from "react";
import {API_KEY} from "../../utlis";

function TestFormData() {
  const [features ,setfeatures]=useState({})
  const [fet_val, setfet_val] = useState({});
  const [Pred ,setPred]=useState("")

  useEffect(()=>{
     let call_features=async()=>{
       let data=await axios.get(`${API_KEY}send_form_features`)
       setfeatures(data.data)

     }
     call_features()
  },[])

  let handle_submit=async(e)=>{
     e.preventDefault();
     for (let key in fet_val) {
          if(fet_val[key]==""){
            alert('please enter all the values')
            return
          }
      }

      let api_Call=await axios.post(`${API_KEY}/predict_form_dat` ,fet_val)
      setPred(api_Call.data)
      console.log(api_Call.data)
  }

  useEffect(() => {
    const initialValues = {};
    if(features.length>0){
      features.forEach((val) => {
      initialValues[val] = "";
    });
    setfet_val(initialValues);
    }
  }, [features]);

  let handle_input = (feature, value) => {
    setfet_val((prev) => ({
      ...prev,
      [feature]: value,
    }));
  };

  const handle_go_back=(e)=>{
    e.preventDefault()
    setPred("")
  }



  return (
   <>
    {Pred ==""? <>
        <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <form
        onSubmit={handle_submit}
        className="bg-white shadow-lg rounded-2xl p-8 w-full max-w-md"
      >
        <h2 className="text-2xl font-semibold text-gray-800 mb-6 text-center">
          Enter Feature Data
        </h2>

        <div className="space-y-4">
          {features.length>0 && features.map((value, index) => (
            <div key={index} className="flex flex-col">
              <label className="mb-1 text-gray-600 font-medium">
                {value.toUpperCase()}
              </label>
              <input
                type="number"
                placeholder={`Enter ${value}`}
                className="border border-gray-300 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
                onChange={(e) => {
                  handle_input(value, e.target.value);
                }}
              />
            </div>
          ))}
        </div>

        <button
          type="submit"
          className="mt-6 w-full bg-blue-600 text-white py-2 rounded-xl font-medium hover:bg-blue-700 transition"
        >
          Predict
        </button>
      </form>
    </div>
    </> :<>
    <div className="flex justify-center items-center min-h-screen bg-gray-100">
      <div className="bg-white p-10 rounded-2xl shadow-lg text-center">
        <h2 className="text-xl font-semibold text-gray-800 mb-3">
          Prediction Result
        </h2>
        <p className="text-2xl font-bold text-blue-600">{Pred["pred"]}</p>
        <button  className="mt-6 w-full bg-cyan-600 text-white py-2 rounded-xl font-medium hover:bg-blue-700 transition" onClick={handle_go_back}>Try for new Value</button>
      </div>
    </div> </>}
   </>
  );
}

export default TestFormData;
