import React from 'react';
import { AppBar, Toolbar, Typography, Button, Container, Box } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';
import GavelIcon from '@mui/icons-material/Gavel';

const Header = () => {
  return (
    <AppBar position="static">
      <Container maxWidth="lg">
        <Toolbar>
          <Box sx={{ display: 'flex', alignItems: 'center', flexGrow: 1 }}>
            <GavelIcon sx={{ mr: 1 }} />
            <Typography
              variant="h6"
              component={RouterLink}
              to="/"
              sx={{
                textDecoration: 'none',
                color: 'white',
                fontWeight: 'bold',
              }}
            >
              Türkiye Hukuk AI Platformu
            </Typography>
          </Box>
          <Box sx={{ display: { xs: 'none', md: 'flex' } }}>
            <Button
              component={RouterLink}
              to="/dilekce-uretici"
              color="inherit"
              sx={{ mx: 1 }}
            >
              Dilekçe Üretici
            </Button>
            <Button
              component={RouterLink}
              to="/sozlesme-analizi"
              color="inherit"
              sx={{ mx: 1 }}
            >
              Sözleşme Analizi
            </Button>
            <Button
              component={RouterLink}
              to="/hukuki-chatbot"
              color="inherit"
              sx={{ mx: 1 }}
            >
              Hukuki Chatbot
            </Button>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};

export default Header;
