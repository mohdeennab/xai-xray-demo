import React, { useState } from 'react';

const ImageUploader = () => {
    const [selectedImage, setSelectedImage] = useState(null);
    const [prediction, setPrediction] = useState(null);
    const [explanation, setExplanation] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onloadend = () => {
                setSelectedImage(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleUpload = async () => {
        if (!selectedImage) return;

        // Mocking prediction and explanation
        // Replace with actual API call
        const mockPrediction = 'Predicted Label';
        const mockExplanation = 'Explanation of the prediction';

        // Simulate API call delay
        setTimeout(() => {
            setPrediction(mockPrediction);
            setExplanation(mockExplanation);
        }, 1000);
    };

    return (
        <div>
            <h2>Image Uploader</h2>
            <input type="file" accept="image/*" onChange={handleImageChange} />
            {selectedImage && <img src={selectedImage} alt="Selected" style={{ width: '300px', height: 'auto' }} />}
            <button onClick={handleUpload}>Upload Image</button>
            {prediction && <p>Prediction: {prediction}</p>}
            {explanation && <p>Explanation: {explanation}</p>}
        </div>
    );
};

export default ImageUploader;