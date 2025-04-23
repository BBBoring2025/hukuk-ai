import React, { useState, useEffect } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Stepper, 
  Step, 
  StepLabel, 
  Button, 
  Paper, 
  Grid, 
  Card, 
  CardContent, 
  CardActions, 
  TextField, 
  MenuItem, 
  FormControl, 
  FormControlLabel, 
  Checkbox, 
  Divider, 
  CircularProgress,
  Alert,
  Chip,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  Accordion,
  AccordionSummary,
  AccordionDetails,
  LinearProgress,
  Tabs,
  Tab
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { 
  Description as DescriptionIcon,
  Upload as UploadIcon,
  Search as SearchIcon,
  Warning as WarningIcon,
  Info as InfoIcon,
  Error as ErrorIcon,
  CheckCircle as CheckCircleIcon,
  ExpandMore as ExpandMoreIcon,
  PictureAsPdf as PdfIcon,
  InsertDriveFile as DocIcon,
  TextSnippet as TextIcon,
  Download as DownloadIcon,
  Compare as CompareIcon,
  Edit as EditIcon
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
  transition: 'background-color 0.3s ease',
  '&:hover': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const RiskIndicator = styled(Box)(({ theme, risk }) => {
  let color = theme.palette.success.main; // Default low risk
  
  if (risk > 70) {
    color = theme.palette.error.main; // High risk
  } else if (risk > 40) {
    color = theme.palette.warning.main; // Medium risk
  }
  
  return {
    position: 'relative',
    height: '100%',
    width: '100%',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    '& .risk-circle': {
      width: 120,
      height: 120,
      borderRadius: '50%',
      border: `8px solid ${color}`,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      marginBottom: theme.spacing(2),
    },
    '& .risk-text': {
      color: color,
      fontWeight: 'bold',
    }
  };
}));

const ClauseCard = styled(Card)(({ theme, riskLevel }) => {
  let borderColor = theme.palette.info.light; // Default info
  
  if (riskLevel === 'critical') {
    borderColor = theme.palette.error.main;
  } else if (riskLevel === 'medium') {
    borderColor = theme.palette.warning.main;
  } else if (riskLevel === 'low') {
    borderColor = theme.palette.success.main;
  }
  
  return {
    marginBottom: theme.spacing(2),
    borderLeft: `4px solid ${borderColor}`,
  };
});

// Main component
const ContractAnalysis = () => {
  // State
  const [activeStep, setActiveStep] = useState(0);
  const [file, setFile] = useState(null);
  const [fileId, setFileId] = useState(null);
  const [contractType, setContractType] = useState('auto');
  const [analysisScope, setAnalysisScope] = useState(['general', 'legal', 'missing']);
  const [analysisDepth, setAnalysisDepth] = useState('standard');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [tabValue, setTabValue] = useState(0);

  // Contract types
  const contractTypes = [
    { value: 'auto', label: 'Otomatik Tespit' },
    { value: 'kira', label: 'Kira Sözleşmesi' },
    { value: 'is', label: 'İş Sözleşmesi' },
    { value: 'satis', label: 'Satış Sözleşmesi' },
    { value: 'hizmet', label: 'Hizmet Sözleşmesi' },
  ];

  // Analysis scope options
  const scopeOptions = [
    { value: 'general', label: 'Genel risk değerlendirmesi' },
    { value: 'legal', label: 'Yasal uyumluluk kontrolü' },
    { value: 'missing', label: 'Eksik madde kontrolü' },
    { value: 'terminology', label: 'Hukuki terminoloji kontrolü' },
    { value: 'industry', label: 'Sektörel standartlara uygunluk' },
  ];

  // Analysis depth options
  const depthOptions = [
    { value: 'basic', label: 'Temel (Hızlı analiz)' },
    { value: 'standard', label: 'Standart (Detaylı analiz)' },
    { value: 'comprehensive', label: 'Kapsamlı (Uzman seviyesi)' },
  ];

  // Steps
  const steps = ['Sözleşme Yükleme', 'Analiz Parametreleri', 'Analiz Sonuçları'];

  // Handle file upload
  const handleFileUpload = (event) => {
    if (event.target.files && event.target.files[0]) {
      setFile(event.target.files[0]);
    }
  };

  // Handle drag and drop
  const handleDrop = (event) => {
    event.preventDefault();
    if (event.dataTransfer.files && event.dataTransfer.files[0]) {
      setFile(event.dataTransfer.files[0]);
    }
  };

  const handleDragOver = (event) => {
    event.preventDefault();
  };

  // Handle analysis scope change
  const handleScopeChange = (event) => {
    const { value, checked } = event.target;
    setAnalysisScope(prev => {
      if (checked) {
        return [...prev, value];
      } else {
        return prev.filter(item => item !== value);
      }
    });
  };

  // Handle tab change
  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  // Upload file to server
  const uploadFile = async () => {
    if (!file) {
      setError('Lütfen bir dosya seçin');
      return false;
    }
    
    setLoading(true);
    setError(null);
    
    const formData = new FormData();
    formData.append('file', file);
    
    try {
      const response = await axios.post(`${API_URL}/upload`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      
      setFileId(response.data.file_id);
      setLoading(false);
      return true;
    } catch (err) {
      console.error('File upload error:', err);
      setError('Dosya yüklenirken bir hata oluştu');
      setLoading(false);
      return false;
    }
  };

  // Analyze contract
  const analyzeContract = async () => {
    if (!fileId) {
      setError('Önce dosya yüklemelisiniz');
      return false;
    }
    
    setLoading(true);
    setError(null);
    
    const analysisData = {
      contract_type: contractType,
      analysis_scope: analysisScope,
      analysis_depth: analysisDepth,
      additional_info: {}
    };
    
    try {
      const response = await axios.post(`${API_URL}/analyze/${fileId}`, analysisData);
      setAnalysisResult(response.data);
      setLoading(false);
      return true;
    } catch (err) {
      console.error('Analysis error:', err);
      setError('Sözleşme analiz edilirken bir hata oluştu');
      setLoading(false);
      return false;
    }
  };

  // Get risk level icon
  const getRiskIcon = (riskLevel) => {
    switch (riskLevel) {
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

  // Navigation
  const handleNext = async () => {
    if (activeStep === 0) {
      const success = await uploadFile();
      if (success) {
        setActiveStep((prevActiveStep) => prevActiveStep + 1);
      }
    } else if (activeStep === 1) {
      const success = await analyzeContract();
      if (success) {
        setActiveStep((prevActiveStep) => prevActiveStep + 1);
      }
    } else {
      setActiveStep((prevActiveStep) => prevActiveStep + 1);
    }
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
    setFile(null);
    setFileId(null);
    setContractType('auto');
    setAnalysisScope(['general', 'legal', 'missing']);
    setAnalysisDepth('standard');
    setAnalysisResult(null);
    setError(null);
  };

  // Render step content
  const getStepContent = (step) => {
    switch (step) {
      case 0:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Sözleşme Dosyasını Yükleyin
            </Typography>
            
            <UploadBox
              onDrop={handleDrop}
              onDragOver={handleDragOver}
              onClick={() => document.getElementById('file-upload').click()}
            >
              <input
                id="file-upload"
                type="file"
                accept=".pdf,.docx,.txt,.md"
                onChange={handleFileUpload}
                style={{ display: 'none' }}
              />
              
              <UploadIcon fontSize="large" color="primary" />
              <Typography variant="h6" color="primary" gutterBottom>
                Dosyayı buraya sürükleyin veya seçmek için tıklayın
              </Typography>
              <Typography variant="body2" color="textSecondary">
                Desteklenen formatlar: PDF, DOCX, TXT, MD
              </Typography>
            </UploadBox>
            
            {file && (
              <Box mt={2} p={2} bgcolor="background.paper" borderRadius={1}>
                <Grid container alignItems="center" spacing={2}>
                  <Grid item>
                    {file.name.endsWith('.pdf') ? (
                      <PdfIcon color="error" />
                    ) : file.name.endsWith('.docx') ? (
                      <DocIcon color="primary" />
                    ) : (
                      <TextIcon color="action" />
                    )}
                  </Grid>
                  <Grid item xs>
                    <Typography variant="subtitle2">{file.name}</Typography>
                    <Typography variant="body2" color="textSecondary">
                      {(file.size / 1024).toFixed(2)} KB
                    </Typography>
                  </Grid>
                  <Grid item>
                    <Button 
                      size="small" 
                      color="secondary" 
                      onClick={() => setFile(null)}
                    >
                      Kaldır
                    </Button>
                  </Grid>
                </Grid>
              </Box>
            )}
          </>
        );
      
      case 1:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Analiz Parametrelerini Belirleyin
            </Typography>
            
            <Grid container spacing={3}>
              <Grid item xs={12} md={6}>
                <TextField
                  select
                  fullWidth
                  label="Sözleşme Türü"
                  value={contractType}
                  onChange={(e) => setContractType(e.target.value)}
                  margin="normal"
                  variant="outlined"
                  helperText="Sözleşme türünü seçin veya otomatik tespit edin"
                >
                  {contractTypes.map((option) => (
                    <MenuItem key={option.value} value={option.value}>
                      {option.label}
                    </MenuItem>
                  ))}
                </TextField>
              </Grid>
              
              <Grid item xs={12} md={6}>
                <TextField
                  select
                  fullWidth
                  label="Analiz Derinliği"
                  value={analysisDepth}
                  onChange={(e) => setAnalysisDepth(e.target.value)}
                  margin="normal"
                  variant="outlined"
                  helperText="Analiz detay seviyesini seçin"
                >
                  {depthOptions.map((option) => (
                    <MenuItem key={option.value} value={option.value}>
                      {option.label}
                    </MenuItem>
                  ))}
                </TextField>
              </Grid>
              
              <Grid item xs={12}>
                <Typography variant="subtitle1" gutterBottom>
                  Analiz Kapsamı
                </Typography>
                <Box display="flex" flexWrap="wrap" gap={2}>
                  {scopeOptions.map((option) => (
                    <FormControlLabel
                      key={option.value}
                      control={
                        <Checkbox
                          checked={analysisScope.includes(option.value)}
                          onChange={handleScopeChange}
                          value={option.value}
                        />
                      }
                      label={option.label}
                    />
                  ))}
                </Box>
              </Grid>
              
              <Grid item xs={12}>
                <Typography variant="subtitle1" gutterBottom>
                  Ek Bilgiler (Opsiyonel)
                </Typography>
                <TextField
                  fullWidth
                  label="Sözleşme Tarafları"
                  placeholder="Örn: Kiracı ve Kiraya Veren"
                  margin="normal"
                  variant="outlined"
                />
                <TextField
                  fullWidth
                  label="Sözleşme Amacı"
                  placeholder="Örn: Konut Kiralaması"
                  margin="normal"
                  variant="outlined"
                />
              </Grid>
            </Grid>
          </>
        );
      
      case 2:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Analiz Sonuçları
            </Typography>
            
            {loading ? (
              <Box display="flex" flexDirection="column" alignItems="center" my={4}>
                <CircularProgress />
                <Typography variant="body2" color="textSecondary" mt={2}>
                  Sözleşme analiz ediliyor...
                </Typography>
              </Box>
            ) : error ? (
              <Alert severity="error" sx={{ my: 2 }}>{error}</Alert>
            ) : analysisResult ? (
              <>
                <Box mb={4}>
                  <Grid container spacing={3}>
                    <Grid item xs={12} md={4}>
                      <RiskIndicator risk={parseInt(analysisResult.risk_level)}>
                        <div className="risk-circle">
                          <Typography variant="h4" className="risk-text">
                            {analysisResult.risk_level}
                          </Typography>
                        </div>
                        <Typography variant="h6" className="risk-text">
                          Risk Skoru
                        </Typography>
                        <Typography variant="body2" align="center" mt={1}>
                          {parseInt(analysisResult.risk_level) > 70 ? (
                            "Yüksek Risk"
                          ) : parseInt(analysisResult.risk_level) > 40 ? (
                            "Orta Risk"
                          ) : (
                            "Düşük Risk"
                          )}
                        </Typography>
                      </RiskIndicator>
                    </Grid>
                    
                    <Grid item xs={12} md={8}>
                      <Typography variant="subtitle1" gutterBottom>
                        Özet
                      </Typography>
                      <Typography variant="body2" paragraph>
                        {analysisResult.summary}
                      </Typography>
                      
                      <Grid container spacing={2} mt={1}>
                        <Grid item xs={6} sm={3}>
                          <Paper elevation={0} sx={{ p: 1, textAlign: 'center', bgcolor: 'error.light' }}>
                            <Typography variant="h5">{analysisResult.critical_issues}</Typography>
                            <Typography variant="body2">Kritik Sorun</Typography>
                          </Paper>
                        </Grid>
                        <Grid item xs={6} sm={3}>
                          <Paper elevation={0} sx={{ p: 1, textAlign: 'center', bgcolor: 'warning.light' }}>
                            <Typography variant="h5">{analysisResult.medium_issues}</Typography>
                            <Typography variant="body2">Orta Sorun</Typography>
                          </Paper>
                        </Grid>
                        <Grid item xs={6} sm={3}>
                          <Paper elevation={0} sx={{ p: 1, textAlign: 'center', bgcolor: 'success.light' }}>
                            <Typography variant="h5">{analysisResult.low_issues}</Typography>
                            <Typography variant="body2">Düşük Sorun</Typography>
                          </Paper>
                        </Grid>
                        <Grid item xs={6} sm={3}>
                          <Paper elevation={0} sx={{ p: 1, textAlign: 'center', bgcolor: 'info.light' }}>
                            <Typography variant="h5">{analysisResult.info_notes}</Typography>
                            <Typography variant="body2">Bilgi Notu</Typography>
                          </Paper>
                        </Grid>
                      </Grid>
                    </Grid>
                  </Grid>
                </Box>
                
                <Divider sx={{ my: 3 }} />
                
                <Box sx={{ width: '100%' }}>
                  <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <Tabs value={tabValue} onChange={handleTabChange} aria-label="analysis tabs">
                      <Tab label="Madde Analizi" />
                      <Tab label="Yasal Uyumluluk" />
                      <Tab label="Düzeltme Önerileri" />
                    </Tabs>
                  </Box>
                  
                  {/* Madde Analizi Tab */}
                  {tabValue === 0 && (
                    <Box p={2}>
                      <Typography variant="subtitle1" gutterBottom>
                        Sözleşme Maddeleri ve Riskler
                      </Typography>
                      
                      {analysisResult.clauses.map((clause) => (
                        <ClauseCard key={clause.id} riskLevel={clause.risk_level}>
                          <CardContent>
                            <Box display="flex" alignItems="center" mb={1}>
                              {getRiskIcon(clause.risk_level)}
                              <Typography variant="subtitle1" ml={1}>
                                Madde {clause.clause_number}
                                {clause.title && `: ${clause.title}`}
                              </Typography>
                            </Box>
                            
                            <Typography variant="body2" color="textSecondary" paragraph>
                              {clause.content.length > 200 
                                ? `${clause.content.substring(0, 200)}...` 
                                : clause.content}
                            </Typography>
                            
                            {clause.issues.length > 0 && (
                              <>
                                <Typography variant="subtitle2" gutterBottom>
                                  Tespit Edilen Sorunlar:
                                </Typography>
                                <List dense>
                                  {clause.issues.map((issue, index) => (
                                    <ListItem key={index}>
                                      <ListItemIcon sx={{ minWidth: 30 }}>
                                        {getRiskIcon(clause.risk_level)}
                                      </ListItemIcon>
                                      <ListItemText primary={issue.message} />
                                    </ListItem>
                                  ))}
                                </List>
                              </>
                            )}
                          </CardContent>
                          {clause.suggestions.length > 0 && (
                            <CardActions>
                              <Button 
                                size="small" 
                                startIcon={<EditIcon />}
                                color="primary"
                              >
                                Düzeltme Önerilerini Gör
                              </Button>
                            </CardActions>
                          )}
                        </ClauseCard>
                      ))}
                    </Box>
                  )}
                  
                  {/* Yasal Uyumluluk Tab */}
                  {tabValue === 1 && (
                    <Box p={2}>
                      <Typography variant="subtitle1" gutterBottom>
                        Yasal Uyumluluk Kontrolü
                      </Typography>
                      
                      <List>
                        {Object.entries(analysisResult.legal_compliance).map(([law, compliant]) => (
                          <ListItem key={law}>
                            <ListItemIcon>
                              {compliant ? (
                                <CheckCircleIcon color="success" />
                              ) : (
                                <ErrorIcon color="error" />
                              )}
                            </ListItemIcon>
                            <ListItemText 
                              primary={law} 
                              secondary={compliant 
                                ? "Sözleşme bu kanunun gerekliliklerine uygun görünüyor" 
                                : "Sözleşme bu kanunun bazı gerekliliklerini karşılamıyor olabilir"
                              } 
                            />
                          </ListItem>
                        ))}
                      </List>
                    </Box>
                  )}
                  
                  {/* Düzeltme Önerileri Tab */}
                  {tabValue === 2 && (
                    <Box p={2}>
                      <Typography variant="subtitle1" gutterBottom>
                        Düzeltme Önerileri
                      </Typography>
                      
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <Typography color="error">Kritik Düzeltmeler</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <List dense>
                            {analysisResult.clauses
                              .filter(clause => clause.risk_level === 'critical')
                              .flatMap(clause => 
                                clause.suggestions.map((suggestion, index) => (
                                  <ListItem key={`${clause.id}-${index}`}>
                                    <ListItemIcon>
                                      <ErrorIcon color="error" />
                                    </ListItemIcon>
                                    <ListItemText 
                                      primary={`Madde ${clause.clause_number}: ${suggestion}`} 
                                    />
                                  </ListItem>
                                ))
                              )}
                          </List>
                        </AccordionDetails>
                      </Accordion>
                      
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <Typography color="warning.main">Orta Seviye Düzeltmeler</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <List dense>
                            {analysisResult.clauses
                              .filter(clause => clause.risk_level === 'medium')
                              .flatMap(clause => 
                                clause.suggestions.map((suggestion, index) => (
                                  <ListItem key={`${clause.id}-${index}`}>
                                    <ListItemIcon>
                                      <WarningIcon color="warning" />
                                    </ListItemIcon>
                                    <ListItemText 
                                      primary={`Madde ${clause.clause_number}: ${suggestion}`} 
                                    />
                                  </ListItem>
                                ))
                              )}
                          </List>
                        </AccordionDetails>
                      </Accordion>
                      
                      <Accordion>
                        <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                          <Typography color="success.main">Düşük Seviye İyileştirmeler</Typography>
                        </AccordionSummary>
                        <AccordionDetails>
                          <List dense>
                            {analysisResult.clauses
                              .filter(clause => clause.risk_level === 'low')
                              .flatMap(clause => 
                                clause.suggestions.map((suggestion, index) => (
                                  <ListItem key={`${clause.id}-${index}`}>
                                    <ListItemIcon>
                                      <InfoIcon color="success" />
                                    </ListItemIcon>
                                    <ListItemText 
                                      primary={`Madde ${clause.clause_number}: ${suggestion}`} 
                                    />
                                  </ListItem>
                                ))
                              )}
                          </List>
                        </AccordionDetails>
                      </Accordion>
                      
                      <Box mt={3} display="flex" justifyContent="center">
                        <Button 
                          variant="contained" 
                          color="primary" 
                          startIcon={<DownloadIcon />}
                        >
                          Düzeltme Raporu İndir
                        </Button>
                      </Box>
                    </Box>
                  )}
                </Box>
              </>
            ) : (
              <Alert severity="info">Analiz sonuçları burada görüntülenecek</Alert>
            )}
          </>
        );
      
      default:
        return 'Bilinmeyen adım';
    }
  };

  return (
    <Container maxWidth="lg">
      <Box my={4}>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Sözleşme Analizi
        </Typography>
        <Typography variant="subtitle1" align="center" color="text.secondary" paragraph>
          Sözleşmelerinizi yapay zeka ile analiz edin, riskleri tespit edin
        </Typography>
      </Box>
      
      <StyledPaper>
        <Stepper activeStep={activeStep} alternativeLabel>
          {steps.map((label) => (
            <Step key={label}>
              <StepLabel>{label}</StepLabel>
            </Step>
          ))}
        </Stepper>
        
        <Box mt={4}>
          {getStepContent(activeStep)}
        </Box>
        
        {error && (
          <Alert severity="error" sx={{ mt: 2 }}>{error}</Alert>
        )}
        
        <Box mt={4} display="flex" justifyContent="space-between">
          <Button
            disabled={activeStep === 0 || loading}
            onClick={handleBack}
          >
            Geri
          </Button>
          <Box>
            {activeStep === steps.length - 1 ? (
              <Button 
                variant="contained" 
                color="primary" 
                onClick={handleReset}
                disabled={loading}
              >
                Yeni Analiz
              </Button>
            ) : (
              <Button
                variant="contained"
                color="primary"
                onClick={handleNext}
                disabled={(activeStep === 0 && !file) || loading}
              >
                {activeStep === steps.length - 2 ? 'Analiz Et' : 'Devam Et'}
                {loading && <CircularProgress size={24} sx={{ ml: 1 }} />}
              </Button>
            )}
          </Box>
        </Box>
      </StyledPaper>
    </Container>
  );
};

export default ContractAnalysis;
