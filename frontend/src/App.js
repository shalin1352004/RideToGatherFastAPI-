import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [profiles, setProfiles] = useState([]);
  const [userId, setUserId] = useState('');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchProfiles();
  }, []);

  const fetchProfiles = async () => {
    try {
      const response = await fetch('http://localhost:8000/profile/1'); // Assuming user_id 1 for demo
      if (response.ok) {
        const data = await response.json();
        setProfiles([data]);
      }
    } catch (error) {
      console.error('Error fetching profiles:', error);
    }
  };

  const handleUpload = async (e) => {
    e.preventDefault();
    if (!file || !userId || !name || !email) return;

    setLoading(true);
    const formData = new FormData();
    formData.append('user_id', userId);
    formData.append('name', name);
    formData.append('email', email);
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:8000/upload-profile-image/', {
        method: 'POST',
        body: formData,
      });
      if (response.ok) {
        const data = await response.json();
        alert('Upload successful!');
        fetchProfiles(); // Refresh profiles
      } else {
        alert('Upload failed');
      }
    } catch (error) {
      console.error('Error uploading:', error);
      alert('Upload error');
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>RideToGather Profile Upload</h1>
      <form onSubmit={handleUpload}>
        <input
          type="text"
          placeholder="User ID"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files[0])}
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Uploading...' : 'Upload'}
        </button>
      </form>
      <h2>Profiles</h2>
      <div className="profiles-container">
        {profiles.map((profile, index) => (
          <div key={index} className="profile-card">
            <p>Name: {profile.name}</p>
            <p>Email: {profile.email}</p>
            {profile.image_url && <img src={profile.image_url} alt="Profile" />}
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
