import React from 'react';
import { Routes, Route } from 'react-router-dom';
import { Container, Box } from '@mui/material';
import Header from './components/Header';
import Footer from './components/Footer';
import HomePage from './components/HomePage';
import PetitionGenerator from './components/PetitionGenerator';
import ContractAnalysis from './components/ContractAnalysis';
import LegalChatbot from './components/LegalChatbot';

function App() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <Header />
      <Container component="main" sx={{ flexGrow: 1, py: 4 }}>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/dilekce-uretici" element={<PetitionGenerator />} />
          <Route path="/sozlesme-analizi" element={<ContractAnalysis />} />
          <Route path="/hukuki-chatbot" element={<LegalChatbot />} />
        </Routes>
      </Container>
      <Footer />
    </Box>
  );
}

export default App;
