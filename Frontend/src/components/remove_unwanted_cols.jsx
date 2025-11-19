import React, { useEffect, useState } from "react";
import axios from "axios";
import Report from "./report";
import {API_KEY} from "../../utlis";

function RemoveUnwantedCols() {
  const [cols, setCols] = useState([]);
  const [selectedCols, setSelectedCols] = useState([]);
  const [loading, setLoading] = useState(true);
  const[change , setChange]=useState(0)
  const[api1  , setapi1 ]=useState(0)
  // Fetch column list from localStorage on mount
  useEffect(() => {
    const stored = localStorage.getItem("columns");
    if (stored) {
      try {
        const parsed = JSON.parse(stored);
        setCols(parsed);
        setSelectedCols(parsed);
      } catch (e) {
        setCols([]);
        setSelectedCols([]);
      }
    } else {
      setCols([]);
      setSelectedCols([]);
    }
    setLoading(false);
  }, []);
  // Handle checkbox toggle
  const handleToggle = (col) => {
    if (selectedCols.includes(col)) {
      setSelectedCols(selectedCols.filter((c) => c !== col));
    } else {
      setSelectedCols([...selectedCols, col]);
    }
  };

 
  const handleSubmit = async (e) => {
    e.preventDefault();
    const notselectedCols = cols.filter((col) => !selectedCols.includes(col));

    try {
      const api = `${API_KEY}/Predict_csv_file`;
      setChange(1)
      const res = await axios.post(
            api,
            { columns: notselectedCols },
              {
            headers: { "Content-Type": "application/json" },
              withCredentials: true,
          }
       );
       
       if (res.status === 200) {
         setapi1(1)
         localStorage.setItem('api',1)
      }
      
      localStorage.setItem('change' ,1)
      
    } catch (err) {
      console.error(err);
      alert("Error submitting unselected columns");
    }
  };

  // Handle form submit
  // const handleSubmit = async (e) => {
  //   e.preventDefault();
  //   try {
  //     const api = "http://127.0.0.1:5000/remove_columns"; // your POST API
  //     const res = await axios.post(api, { columns: selectedCols });
  //     if (res.status === 200) {
  //       alert("Columns updated successfully!");
  //     }
  //   } catch (err) {
  //     console.error(err);
  //     alert("Error submitting selected columns");
  //   }
  // };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-900 text-white">
        Loading columns...
      </div>
    );
  }

  return (
    <>
      {change==0 && !localStorage.getItem('change')?<div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-black to-gray-800 p-6">
      <form
        onSubmit={handleSubmit}
        className="bg-white/10 backdrop-blur-xl border border-white/20 rounded-2xl p-8 w-full max-w-lg shadow-2xl"
      >
        <h2 className="text-2xl font-semibold text-white mb-6 text-center">
          Select Columns to Keep (please remove cols like id date etc to get good accurcay)
        </h2>
        <div className="space-y-3 max-h-96 overflow-y-auto mb-6">
          {cols.map((col, idx) => (
            <label
              key={idx}
              className="flex items-center justify-between bg-white/10 hover:bg-white/20 px-4 py-2 rounded-lg cursor-pointer transition"
            >
              <span className="text-gray-200">{col}</span>
              <input
                type="checkbox"
                checked={selectedCols.includes(col)}
                onChange={() => handleToggle(col)}
                className="w-5 h-5 accent-green-500"
              />
            </label>
          ))}
        </div>
        <button
          type="submit"
          className="w-full bg-gradient-to-r from-green-500 to-yellow-500 hover:from-green-600 hover:to-yellow-600 text-black font-semibold py-2 px-4 rounded-lg shadow-lg transition duration-200"
        >
          Submit
        </button>
      </form>
    </div>:<Report api={api1}/>}
    
    </>
  );
}

export default RemoveUnwantedCols;
