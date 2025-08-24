import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import ReactDOM from 'react-dom/client'
import './index.css'
import TestFormData from './components/Testingpage.jsx'
import {createBrowserRouter,RouterProvider} from 'react-router-dom'
import Training_page from './components/TrainingPage.jsx'
import DataInputSelector from './components/Testingpage.jsx'
import Report from './components/report.jsx'
import Homepage from './components/Homepage.jsx'

let route=createBrowserRouter([
  {
    path:'/',
    element : <Homepage/>,
   
     
    
  },
      {
        path:'/train',
        element:<Training_page/>
      },
      {
        path:'/report',
        element:<Report/>
      },
      {
        path:'/test_form_data',
        element:<TestFormData/>
      }
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <StrictMode>
    <RouterProvider router={route}/>
  </StrictMode>,
)
