import React from "react";

export default function UploadPDFCard() {
    return (
        <div className="flex items-center justify-center min-h-screen bg-[#f8f9fa]">
            <div className=" min-h-screen p-8 w-1/2">
                <h2 className="text-[#6c757d] text-lg mb-4">Select a bill to analyse</h2>
                <div className="bg-white rounded-[12px] shadow-md p-6">
                <div className="bg-[#f8f9fa] rounded-[12px] p-4 mb-4">
                    <div className="flex items-center mb-4">
                    <i className="fas fa-upload text-[#6c757d] mr-2"></i>
                    <span className="text-[#6c757d]">Extract data from PDF</span>
                    </div>
                    <h3 className="text-[#6c757d] text-lg mb-4">Upload legislative document</h3>
                    <div className="border-dashed border-2 border-[#6c757d] rounded-[12px] p-10 text-center m-8">
                    <i className="fas fa-cloud-upload-alt text-[#6c757d] text-4xl mb-4"></i>
                    <p className="text-[#6c757d]">Drag and drop PDFs<br />Or click to browse files</p>
                    </div>
                    <button className="bg-[#6c757d] text-white py-2 px-4 rounded-[8px]">Upload PDF</button>
                </div>
                <div className="flex items-center">
                    <i className="fas fa-list text-[#6c757d] mr-2"></i>
                    <span className="text-[#6c757d]">List of concepts</span>
                </div>
                </div>
                <button className="bg-[#6c757d] text-white p-4 rounded-full fixed bottom-8 right-8">
                <i className="fas fa-arrow-right"></i>
                </button>
            </div>
        </div>
);
  }