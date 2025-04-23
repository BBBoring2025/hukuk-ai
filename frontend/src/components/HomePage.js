import React from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Grid, 
  Card, 
  CardContent, 
  CardMedia, 
  CardActionArea,
  Button,
  Paper
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import DescriptionIcon from '@mui/icons-material/Description';
import GavelIcon from '@mui/icons-material/Gavel';
import ChatIcon from '@mui/icons-material/Chat';

const HomePage = () => {
  const navigate = useNavigate();

  return (
    <Container maxWidth="lg">
      {/* Hero Section */}
      <Paper 
        elevation={3}
        sx={{
          p: 4,
          mb: 6,
          mt: 2,
          borderRadius: 2,
          background: 'linear-gradient(45deg, #1976d2 30%, #2196f3 90%)',
          color: 'white'
        }}
      >
        <Grid container spacing={3} alignItems="center">
          <Grid item xs={12} md={8}>
            <Typography variant="h3" component="h1" gutterBottom>
              Türkiye Hukuk AI Platformu
            </Typography>
            <Typography variant="h6" paragraph>
              Yapay zeka destekli hukuki çözümlerle hukuk süreçlerinizi kolaylaştırın.
              Dilekçe üretici, sözleşme analizi ve hukuki chatbot araçlarımızla hukuki işlemlerinizi hızlandırın.
            </Typography>
            <Button 
              variant="contained" 
              color="secondary" 
              size="large"
              onClick={() => navigate('/dilekce-uretici')}
              sx={{ mr: 2, mt: 2 }}
            >
              Hemen Başla
            </Button>
          </Grid>
          <Grid item xs={12} md={4}>
            <Box sx={{ display: 'flex', justifyContent: 'center' }}>
              <GavelIcon sx={{ fontSize: 180, opacity: 0.8 }} />
            </Box>
          </Grid>
        </Grid>
      </Paper>

      {/* Services Section */}
      <Typography variant="h4" component="h2" gutterBottom align="center" sx={{ mb: 4 }}>
        Hizmetlerimiz
      </Typography>
      
      <Grid container spacing={4}>
        {/* Dilekçe Üretici */}
        <Grid item xs={12} md={4}>
          <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <CardActionArea onClick={() => navigate('/dilekce-uretici')}>
              <Box sx={{ p: 3, display: 'flex', justifyContent: 'center' }}>
                <DescriptionIcon sx={{ fontSize: 80, color: '#1976d2' }} />
              </Box>
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  Dilekçe Üretici
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  İhtiyacınıza uygun profesyonel dilekçeleri saniyeler içinde oluşturun. 
                  Tüketici şikayetleri, iş hukuku ve kira davaları için hazır şablonlar.
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>

        {/* Sözleşme Analizi */}
        <Grid item xs={12} md={4}>
          <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <CardActionArea onClick={() => navigate('/sozlesme-analizi')}>
              <Box sx={{ p: 3, display: 'flex', justifyContent: 'center' }}>
                <GavelIcon sx={{ fontSize: 80, color: '#1976d2' }} />
              </Box>
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  Sözleşme Analizi
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  Sözleşmelerinizi yapay zeka ile analiz edin, riskli maddeleri tespit edin.
                  Kira, iş ve ticari sözleşmeler için detaylı risk analizi.
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>

        {/* Hukuki Chatbot */}
        <Grid item xs={12} md={4}>
          <Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <CardActionArea onClick={() => navigate('/hukuki-chatbot')}>
              <Box sx={{ p: 3, display: 'flex', justifyContent: 'center' }}>
                <ChatIcon sx={{ fontSize: 80, color: '#1976d2' }} />
              </Box>
              <CardContent>
                <Typography gutterBottom variant="h5" component="h2">
                  Hukuki Chatbot
                </Typography>
                <Typography variant="body1" color="text.secondary">
                  Hukuki sorularınıza anında yanıt alın. İş hukuku, aile hukuku, 
                  tüketici hakları ve daha fazlası hakkında bilgi edinin.
                </Typography>
              </CardContent>
            </CardActionArea>
          </Card>
        </Grid>
      </Grid>

      {/* About Section */}
      <Box sx={{ mt: 8, mb: 4 }}>
        <Typography variant="h4" component="h2" gutterBottom align="center" sx={{ mb: 4 }}>
          Hakkımızda
        </Typography>
        <Typography variant="body1" paragraph>
          Türkiye Hukuk AI Platformu, hukuki süreçleri herkes için daha erişilebilir ve anlaşılır hale getirmeyi amaçlayan
          yenilikçi bir yapay zeka çözümüdür. Platformumuz, avukatlar, KOBİ'ler ve bireysel kullanıcılar için
          özelleştirilmiş hizmetler sunmaktadır.
        </Typography>
        <Typography variant="body1" paragraph>
          Tüm hizmetlerimiz KVKK uyumlu olup, kullanıcı verilerinin gizliliği ve güvenliği en üst düzeyde sağlanmaktadır.
          Yapay zeka modellerimiz, Türk hukuk sistemi ve mevzuatına göre özel olarak eğitilmiştir.
        </Typography>
      </Box>
    </Container>
  );
};

export default HomePage;
