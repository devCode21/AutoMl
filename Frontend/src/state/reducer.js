import { createSlice } from "@reduxjs/toolkit"; 

export const DataFetched=()=>{
    name:'data fetched'
    {
        datafetch:0
    }
    reducers:{
        chnage_value:(state ,action)=>{
            state.datafetch=1
        }
    }
}