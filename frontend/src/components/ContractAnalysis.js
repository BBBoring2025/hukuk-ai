import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  Grid, 
  Button, 
  TextField, 
  CircularProgress, 
  Alert,
  Card,
  CardContent,
  CardActions,
  Divider,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Chip
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { 
  Upload as UploadIcon,
  Description as DescriptionIcon,
  Warning as WarningIcon,
  Info as InfoIcon,
  CheckCircle as CheckCircleIcon,
  Error as ErrorIcon,
  Article as ArticleIcon
} from '@mui/icons-material';
import axios from 'axios';

// API URL
const API_URL = 'http://localhost:8001';

// Styled components
const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  marginBottom: theme.spacing(3),
}));

const UploadBox = styled(Box)(({ theme }) => ({
  border: `2px dashed ${theme.palette.primary.main}`,
  borderRadius: theme.shape.borderRadius,
  padding: theme.spacing(4),
  textAlign: 'center',
  cursor: 'pointer',
  backgroundColor: theme.palette.background.default,
  transition: 'background-color 0.3s ease',
  '&:hover': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const AnalysisResultCard = styled(Card)(({ theme }) => ({
  marginBottom: theme.spacing(2),
  borderLeft: `4px solid ${theme.palette.primary.main}`,
}));

const ClauseCard = styled(Card)(({ theme, risk }) => {
  let borderColor = theme.palette.info.main;
  if (risk === 'critical') borderColor = theme.palette.error.main;
  else if (risk === 'medium') borderColor = theme.palette.warning.main;
  else if (risk === 'low') borderColor = theme.palette.success.main;
  
  return {
    marginBottom: theme.spacing(2),
    borderLeft: `4px solid ${borderColor}`,
  };
});

// Main component
const ContractAnalysis = () => {
  // State
  const [file, setFile] = useState(null);
  const [contractType, setContractType] = useState('kira');
  const [analysisScope, setAnalysisScope] = useState('full');
  const [analysisDepth, setAnalysisDepth] = useState('detailed');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [contractText, setContractText] = useState('');
  const [analysisMode, setAnalysisMode] = useState('file'); // 'file' or 'text'

  // Contract types
  const contractTypes = [
    { value: 'kira', label: 'Kira Sözleşmesi' },
    { value: 'is', label: 'İş Sözleşmesi' },
    { value: 'ticari', label: 'Ticari Sözleşme' },
  ];

  // Handle file selection
  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      setError(null);
    }
  };

  // Handle file drop
  const handleFileDrop = (event) => {
    event.preventDefault();
    const droppedFile = event.dataTransfer.files[0];
    if (droppedFile) {
      setFile(droppedFile);
      setError(null);
    }
  };

  // Prevent default behavior for drag events
  const handleDragOver = (event) => {
    event.preventDefault();
  };

  // Handle contract type change
  const handleContractTypeChange = (event) => {
    setContractType(event.target.value);
  };

  // Handle analysis mode change
  const handleAnalysisModeChange = (mode) => {
    setAnalysisMode(mode);
    setError(null);
  };

  // Handle contract text change
  const handleContractTextChange = (event) => {
    setContractText(event.target.value);
  };

  // Submit analysis
  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    setAnalysisResult(null);

    try {
      let response;

      if (analysisMode === 'file') {
        if (!file) {
          throw new Error('Lütfen bir dosya seçin.');
        }

        const formData = new FormData();
        formData.append('contract_file', file);
        formData.append('contract_type', contractType);
        formData.append('analysis_scope', analysisScope);
        formData.append('analysis_depth', analysisDepth);

        response = await axios.post(`${API_URL}/analyze-contract`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
      } else {
        if (!contractText.trim()) {
          throw new Error('Lütfen sözleşme metnini girin.');
        }

        const formData = new FormData();
        formData.append('contract_text', contractText);
        formData.append('contract_type', contractType);
        formData.append('analysis_scope', analysisScope);
        formData.append('analysis_depth', analysisDepth);

        response = await axios.post(`${API_URL}/analyze-text`, formData);
      }

      setAnalysisResult(response.data);
    } catch (err) {
      console.error('Analysis error:', err);
      setError(err.message || 'Analiz sırasında bir hata oluştu.');
    } finally {
      setLoading(false);
    }
  };

  // Reset form
  const handleReset = () => {
    setFile(null);
    setContractText('');
    setContractType('kira');
    setAnalysisScope('full');
    setAnalysisDepth('detailed');
    setError(null);
    setAnalysisResult(null);
  };

  // Get risk icon
  const getRiskIcon = (risk) => {
    switch (risk) {
      case 'critical':
        return <ErrorIcon color="error" />;
      case 'medium':
        return <WarningIcon color="warning" />;
      case 'low':
        return <InfoIcon color="success" />;
      default:
        return <CheckCircleIcon color="info" />;
    }
  };

  // Get risk color
  const getRiskColor = (risk) => {
    switch (risk) {
      case 'Yüksek Risk':
        return 'error';
      case 'Orta Risk':
        return 'warning';
      case 'Düşük Risk':
        return 'success';
      default:
        return 'info';
    }
  };

  return (
    <Container maxWidth="lg">
      <StyledPaper>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Sözleşme Analizi
        </Typography>
        <Typography variant="body1" paragraph align="center">
          Sözleşmelerinizi yapay zeka ile analiz edin, riskleri tespit edin.
        </Typography>

        {!analysisResult ? (
          <>
            <Box sx={{ mb: 4 }}>
              <Grid container spacing={2}>
                <Grid item xs={12} md={6}>
                  <Button
                    variant={analysisMode === 'file' ? 'contained' : 'outlined'}
                    fullWidth
                    onClick={() => handleAnalysisModeChange('file')}
                    startIcon={<UploadIcon />}
                  >
                    Dosya Yükle
                  </Button>
                </Grid>
                <Grid item xs={12} md={6}>
                  <Button
                    variant={analysisMode === 'text' ? 'contained' : 'outlined'}
                    fullWidth
                    onClick={() => handleAnalysisModeChange('text')}
                    startIcon={<DescriptionIcon />}
                  >
                    Metin Gir
                  </Button>
                </Grid>
              </Grid>
            </Box>

            {analysisMode === 'file' ? (
              <Box sx={{ mb: 4 }}>
                <input
                  type="file"
                  id="contract-file"
                  accept=".pdf,.docx,.doc,.txt"
                  style={{ display: 'none' }}
                  onChange={handleFileChange}
                />
                <label htmlFor="contract-file">
                  <UploadBox
                    onDrop={handleFileDrop}
                    onDragOver={handleDragOver}
                  >
                    <UploadIcon sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
                    <Typography variant="h6" gutterBottom>
                      Sözleşme Dosyasını Sürükleyin veya Tıklayın
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      PDF, DOCX veya TXT formatında dosyalar desteklenir
                    </Typography>
                    {file && (
                      <Box sx={{ mt: 2 }}>
                        <Chip
                          label={file.name}
                          onDelete={() => setFile(null)}
                          color="primary"
                        />
                      </Box>
                    )}
                  </UploadBox>
                </label>
              </Box>
            ) : (
              <Box sx={{ mb: 4 }}>
                <TextField
                  fullWidth
                  multiline
                  rows={10}
                  label="Sözleşme Metni"
                  placeholder="Sözleşme metnini buraya yapıştırın..."
                  value={contractText}
                  onChange={handleContractTextChange}
                  variant="outlined"
                />
              </Box>
            )}

            <Grid container spacing={3}>
              <Grid item xs={12} md={4}>
                <TextField
                  select
                  fullWidth
                  label="Sözleşme Türü"
                  value={contractType}
                  onChange={handleContractTypeChange}
                  variant="outlined"
                  SelectProps={{
                    native: true,
                  }}
                >
                  {contractTypes.map((option) => (
                    <option key={option.value} value={option.value}>
                      {option.label}
                    </option>
                  ))}
                </TextField>
              </Grid>
              <Grid item xs={12} md={4}>
                <TextField
                  select
                  fullWidth
                  label="Analiz Kapsamı"
                  value={analysisScope}
                  onChange={(e) => setAnalysisScope(e.target.value)}
                  variant="outlined"
                  SelectProps={{
                    native: true,
                  }}
                >
                  <option value="full">Tam Analiz</option>
                  <option value="risk">Sadece Risk Analizi</option>
                  <option value="compliance">Sadece Uyumluluk Analizi</option>
                </TextField>
              </Grid>
              <Grid item xs={12} md={4}>
                <TextField
                  select
                  fullWidth
                  label="Analiz Derinliği"
                  value={analysisDepth}
                  onChange={(e) => setAnalysisDepth(e.target.value)}
                  variant="outlined"
                  SelectProps={{
                    native: true,
                  }}
                >
                  <option value="basic">Temel</option>
                  <option value="detailed">Detaylı</option>
                  <option value="expert">Uzman</option>
                </TextField>
              </Grid>
            </Grid>

            {error && (
              <Alert severity="error" sx={{ mt: 3 }}>
                {error}
              </Alert>
            )}

            <Box sx={{ mt: 4, display: 'flex', justifyContent: 'center' }}>
              <Button
                variant="contained"
                color="primary"
                size="large"
                onClick={handleSubmit}
                disabled={loading || (analysisMode === 'file' && !file) || (analysisMode === 'text' && !contractText.trim())}
                startIcon={loading ? <CircularProgress size={24} color="inherit" /> : null}
              >
                {loading ? 'Analiz Ediliyor...' : 'Analiz Et'}
              </Button>
            </Box>
          </>
        ) : (
          <Box>
            <AnalysisResultCard>
              <CardContent>
                <Grid container spacing={2}>
                  <Grid item xs={12} md={8}>
                    <Typography variant="h5" gutterBottom>
                      Sözleşme Analiz Sonucu
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                      Oluşturulma: {new Date(analysisResult.created_at).toLocaleString('tr-TR')}
                    </Typography>
                  </Grid>
                  <Grid item xs={12} md={4} sx={{ display: 'flex', justifyContent: 'flex-end', alignItems: 'center' }}>
                    <Chip
                      label={analysisResult.risk_level}
                      color={getRiskColor(analysisResult.risk_level)}
                      icon={<WarningIcon />}
                      sx={{ fontWeight: 'bold' }}
                    />
                  </Grid>
                </Grid>

                <Divider sx={{ my: 2 }} />

                <Grid container spacing={2}>
                  <Grid item xs={6} sm={3}>
                    <Box sx={{ textAlign: 'center' }}>
                      <Typography variant="h6">{analysisResult.total_clauses}</Typography>
                      <Typography variant="body2">Toplam Madde</Typography>
                    </Box>
                  </Grid>
                  <Grid item xs={6} sm={3}>
                    <Box sx={{ textAlign: 'center' }}>
                      <Typography variant="h6" color="error.main">{analysisResult.critical_issues}</Typography>
                      <Typography variant="body2">Kritik Sorun</Typography>
                    </Box>
                  </Grid>
                  <Grid item xs={6} sm={3}>
                    <Box sx={{ textAlign: 'center' }}>
                      <Typography variant="h6" color="warning.main">{analysisResult.medium_issues}</Typography>
                      <Typography variant="body2">Orta Seviye Sorun</Typography>
                    </Box>
                  </Grid>
                  <Grid item xs={6} sm={3}>
                    <Box sx={{ textAlign: 'center' }}>
                      <Typography variant="h6" color="success.main">{analysisResult.low_issues}</Typography>
                      <Typography variant="body2">Düşük Seviye Not</Typography>
                    </Box>
                  </Grid>
                </Grid>

                <Divider sx={{ my: 2 }} />

                <Typography variant="h6" gutterBottom>
                  Özet
                </Typography>
                <Typography variant="body2" paragraph sx={{ whiteSpace: 'pre-line' }}>
                  {analysisResult.summary}
                </Typography>

                <Typography variant="h6" gutterBottom>
                  Yasal Uyumluluk
                </Typography>
                <Grid container spacing={1}>
                  {Object.entries(analysisResult.legal_compliance).map(([clause, compliant]) => (
                    <Grid item xs={12} sm={6} md={4} key={clause}>
                      <Chip
                        icon={compliant ? <CheckCircleIcon /> : <ErrorIcon />}
                        label={clause}
                        color={compliant ? 'success' : 'error'}
                        variant={compliant ? 'outlined' : 'filled'}
                        sx={{ m: 0.5 }}
                      />
                    </Grid>
                  ))}
                </Grid>
              </CardContent>
            </AnalysisResultCard>

            <Typography variant="h6" gutterBottom>
              Madde Analizi
            </Typography>
            {analysisResult.clauses.map((clause) => (
              <ClauseCard key={clause.id} risk={clause.risk_level}>
                <CardContent>
                  <Grid container spacing={2}>
                    <Grid item xs={12} sm={9}>
                      <Typography variant="subtitle1" gutterBottom>
                        {clause.clause_number}. {clause.title || 'Madde'}
                      </Typography>
                    </Grid>
                    <Grid item xs={12} sm={3} sx={{ display: 'flex', justifyContent: { xs: 'flex-start', sm: 'flex-end' } }}>
                      <Chip
                        icon={getRiskIcon(clause.risk_level)}
                        label={
                          clause.risk_level === 'critical' ? 'Kritik' :
                          clause.risk_level === 'medium' ? 'Orta' :
                          clause.risk_level === 'low' ? 'Düşük' : 'Bilgi'
                        }
                        color={
                          clause.risk_level === 'critical' ? 'error' :
                          clause.risk_level === 'medium' ? 'warning' :
                          clause.risk_level === 'low' ? 'success' : 'info'
                        }
                        size="small"
                      />
                    </Grid>
                  </Grid>

                  <Typography variant="body2" color="text.secondary" paragraph sx={{ mt: 1 }}>
                    {clause.content}
                  </Typography>

                  {clause.issues.length > 0 && (
                    <Box sx={{ mt: 2 }}>
                      <Typography variant="subtitle2" gutterBottom>
                        Tespit Edilen Sorunlar:
                      </Typography>
                      <List dense>
                        {clause.issues.map((issue, index) => (
                          <ListItem key={index}>
                            <ListItemIcon sx={{ minWidth: 36 }}>
                              {issue.type === 'critical' ? <ErrorIcon color="error" /> :
                               issue.type === 'medium' ? <WarningIcon color="warning" /> :
                               <InfoIcon color="info" />}
                            </ListItemIcon>
                            <ListItemText primary={issue.message} />
                          </ListItem>
                        ))}
                      </List>
                    </Box>
                  )}

                  {clause.suggestions.length > 0 && (
                    <Box sx={{ mt: 2 }}>
                      <Typography variant="subtitle2" gutterBottom>
                        Öneriler:
                      </Typography>
                      <List dense>
                        {clause.suggestions.map((suggestion, index) => (
                          <ListItem key={index}>
                            <ListItemIcon sx={{ minWidth: 36 }}>
                              <ArticleIcon color="primary" />
                            </ListItemIcon>
                            <ListItemText primary={suggestion} />
                          </ListItem>
                        ))}
                      </List>
                    </Box>
                  )}
                </CardContent>
              </ClauseCard>
            ))}

            <Box sx={{ mt: 4, display: 'flex', justifyContent: 'center' }}>
              <Button
                variant="contained"
                color="primary"
                onClick={handleReset}
              >
                Yeni Analiz
              </Button>
            </Box>
          </Box>
        )}
      </StyledPaper>
    </Container>
  );
};

export default ContractAnalysis;
