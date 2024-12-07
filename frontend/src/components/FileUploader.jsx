import { useRef, useState } from "react";
import { uploadSVG } from "../assets";
import "../App.css";

const FileUploader = () => {
    const [file, setFile] = useState(null);
    const [diseaseFound, setDisease] = useState('None');
    const fileInputRef = useRef(null);
    
    const handleDragOver = (e) => {
        e.preventDefault();
    };
    
    const handleClick = () => {
        fileInputRef.current.click();
    };
    
    const handleDrop = (e) => {
        e.preventDefault();
        const uploadedFile = e.dataTransfer.files[0];
        setFile(uploadedFile);
    };
    
    const downloadFile = () => {
        if (file) {
          const url = URL.createObjectURL(file);
          const a = document.createElement('a');
          a.href = url;
          a.download = file.name;
          document.body.appendChild(a);
          a.click();
          window.URL.revokeObjectURL(url);
          document.body.removeChild(a);
        }
    };
    
    const handleDeleteFile = () => {
        setFile(null);
    };
    
    const handleFileInputChange = (e) => {
        if (e.target.files.length > 0) {
          const uploadedFile = e.target.files[0];
          setFile(uploadedFile);
        }
    };
    
    const handleSubmit = () => {
        if (!file) {
            alert('Please upload a file first!');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);
        const apiPath = process.env.REACT_APP_BACKEND_LINK;
        fetch(apiPath+'/predict', {  // Ensure the URL matches your Flask server
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const { disease } = data;
            setDisease(disease);
            console.log('Response:', data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    };

    return (
        <div className="UploadFile">
            <div className="FileUploaderDiv" onClick={handleClick} onDrop={handleDrop} onDragOver={handleDragOver}>
                <img src={uploadSVG} alt="upload" className="uploadIMG"/>
                {file ? (
                        <div className="uploadedDataInfoDiv">
                            <p onClick={downloadFile}>File uploaded: {file.name}</p>
                            <p>File type: {file.type}</p>
                            <p onClick={handleDeleteFile} style={{textDecorationLine: 'underline',textDecorationColor: 'black'}}>Delete File</p>
                        </div>
                    ) : (
                        <div className="uploadedDataInfoDiv">
                            <p>Click to Browse or Drop the file</p>
                        </div>
                    )}
                <input type='file' ref={fileInputRef} onChange={handleFileInputChange} accept="image/*" className="FileUploaderDiv" style={{display: 'none'}}/>
            </div>
            <input type='submit' value='Upload' className="submitButton" onClick={handleSubmit}/>
            <p className="ptagDisease">Disease Found: {diseaseFound}</p>
        </div>
    );
}

export default FileUploader;