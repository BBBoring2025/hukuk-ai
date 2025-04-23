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
  RadioGroup, 
  Radio, 
  Divider, 
  CircularProgress,
  Alert
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { 
  Description as DescriptionIcon,
  Category as CategoryIcon,
  Person as PersonIcon,
  Business as BusinessIcon,
  Edit as EditIcon,
  Preview as PreviewIcon,
  Download as DownloadIcon,
  Save as SaveIcon
} from '@mui/icons-material';
import axios from 'axios';

// API URL
const API_URL = 'http://localhost:8000';

// Styled components
const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  marginBottom: theme.spacing(3),
}));

const CategoryCard = styled(Card)(({ theme }) => ({
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  transition: 'transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out',
  '&:hover': {
    transform: 'translateY(-5px)',
    boxShadow: theme.shadows[10],
  },
}));

const TemplateCard = styled(Card)(({ theme }) => ({
  height: '100%',
  display: 'flex',
  flexDirection: 'column',
  transition: 'transform 0.2s ease-in-out',
  cursor: 'pointer',
  '&:hover': {
    transform: 'translateY(-3px)',
    boxShadow: theme.shadows[5],
  },
}));

const PreviewContainer = styled(Box)(({ theme }) => ({
  border: `1px solid ${theme.palette.divider}`,
  padding: theme.spacing(2),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: '#f9f9f9',
  minHeight: '500px',
  maxHeight: '700px',
  overflowY: 'auto',
  fontFamily: 'Times New Roman, serif',
  fontSize: '12pt',
  lineHeight: 1.5,
}));

// Main component
const PetitionGenerator = () => {
  // State
  const [activeStep, setActiveStep] = useState(0);
  const [categories, setCategories] = useState([
    { id: 'tuketici', name: 'Tüketici Hukuku', icon: <PersonIcon /> },
    { id: 'is', name: 'İş Hukuku', icon: <BusinessIcon /> },
    { id: 'kira', name: 'Kira Hukuku', icon: <HomeIcon /> },
    { id: 'aile', name: 'Aile Hukuku', icon: <FamilyIcon /> },
    { id: 'idari', name: 'İdari Hukuk', icon: <GavelIcon /> },
    { id: 'diger', name: 'Diğer', icon: <MoreIcon /> },
  ]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [templates, setTemplates] = useState([]);
  const [selectedTemplate, setSelectedTemplate] = useState(null);
  const [formData, setFormData] = useState({
    userData: {},
    recipientData: {},
    contentData: {},
  });
  const [generatedPetition, setGeneratedPetition] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  // Steps
  const steps = ['Dilekçe Türü Seçimi', 'Kişisel Bilgiler', 'Dilekçe İçeriği', 'Önizleme ve İndirme'];

  // Fetch templates
  useEffect(() => {
    if (selectedCategory) {
      setLoading(true);
      axios.get(`${API_URL}/templates/${selectedCategory.id}`)
        .then(response => {
          setTemplates(response.data);
          setLoading(false);
        })
        .catch(err => {
          console.error('Templates fetch error:', err);
          setError('Şablonlar yüklenirken bir hata oluştu.');
          setLoading(false);
        });
    }
  }, [selectedCategory]);

  // Handle category selection
  const handleCategorySelect = (category) => {
    setSelectedCategory(category);
    setSelectedTemplate(null);
  };

  // Handle template selection
  const handleTemplateSelect = (template) => {
    setSelectedTemplate(template);
    
    // Initialize form data with template fields
    const initialUserData = {};
    const initialRecipientData = {};
    const initialContentData = {};
    
    template.fields.forEach(field => {
      if (field.name.startsWith('muhatap_')) {
        initialRecipientData[field.name] = '';
      } else if (field.name === 'ad_soyad' || field.name === 'tc_kimlik' || 
                field.name === 'adres' || field.name === 'telefon' || 
                field.name === 'eposta') {
        initialUserData[field.name] = '';
      } else {
        initialContentData[field.name] = field.type === 'checkbox' ? [] : '';
      }
    });
    
    setFormData({
      userData: initialUserData,
      recipientData: initialRecipientData,
      contentData: initialContentData,
    });
    
    // Move to next step
    handleNext();
  };

  // Handle form input change
  const handleInputChange = (section, name, value) => {
    setFormData(prevData => ({
      ...prevData,
      [section]: {
        ...prevData[section],
        [name]: value
      }
    }));
  };

  // Handle checkbox change
  const handleCheckboxChange = (section, name, option, checked) => {
    setFormData(prevData => {
      const currentValues = [...(prevData[section][name] || [])];
      
      if (checked) {
        if (!currentValues.includes(option)) {
          currentValues.push(option);
        }
      } else {
        const index = currentValues.indexOf(option);
        if (index !== -1) {
          currentValues.splice(index, 1);
        }
      }
      
      return {
        ...prevData,
        [section]: {
          ...prevData[section],
          [name]: currentValues
        }
      };
    });
  };

  // Generate petition
  const generatePetition = () => {
    setLoading(true);
    setError(null);
    
    const petitionData = {
      template_id: selectedTemplate.id,
      user_data: formData.userData,
      recipient_data: formData.recipientData,
      content_data: formData.contentData,
    };
    
    axios.post(`${API_URL}/generate`, petitionData)
      .then(response => {
        setGeneratedPetition(response.data);
        setLoading(false);
        handleNext();
      })
      .catch(err => {
        console.error('Petition generation error:', err);
        setError('Dilekçe oluşturulurken bir hata meydana geldi.');
        setLoading(false);
      });
  };

  // Download petition
  const downloadPetition = (format = 'pdf') => {
    if (!generatedPetition) return;
    
    window.open(`${API_URL}/download/${generatedPetition.id}?format=${format}`, '_blank');
  };

  // Navigation
  const handleNext = () => {
    if (activeStep === 2) {
      generatePetition();
    } else {
      setActiveStep((prevActiveStep) => prevActiveStep + 1);
    }
  };

  const handleBack = () => {
    setActiveStep((prevActiveStep) => prevActiveStep - 1);
  };

  const handleReset = () => {
    setActiveStep(0);
    setSelectedCategory(null);
    setSelectedTemplate(null);
    setFormData({
      userData: {},
      recipientData: {},
      contentData: {},
    });
    setGeneratedPetition(null);
  };

  // Render form fields
  const renderFormField = (field, section) => {
    const value = formData[section][field.name] || '';
    
    switch (field.type) {
      case 'text':
      case 'email':
      case 'number':
        return (
          <TextField
            key={field.name}
            fullWidth
            label={field.label}
            type={field.type}
            value={value}
            onChange={(e) => handleInputChange(section, field.name, e.target.value)}
            required={field.required}
            margin="normal"
            variant="outlined"
          />
        );
      
      case 'textarea':
        return (
          <TextField
            key={field.name}
            fullWidth
            label={field.label}
            multiline
            rows={4}
            value={value}
            onChange={(e) => handleInputChange(section, field.name, e.target.value)}
            required={field.required}
            margin="normal"
            variant="outlined"
          />
        );
      
      case 'date':
        return (
          <TextField
            key={field.name}
            fullWidth
            label={field.label}
            type="date"
            value={value}
            onChange={(e) => handleInputChange(section, field.name, e.target.value)}
            required={field.required}
            margin="normal"
            variant="outlined"
            InputLabelProps={{
              shrink: true,
            }}
          />
        );
      
      case 'select':
        return (
          <TextField
            key={field.name}
            select
            fullWidth
            label={field.label}
            value={value}
            onChange={(e) => handleInputChange(section, field.name, e.target.value)}
            required={field.required}
            margin="normal"
            variant="outlined"
          >
            {field.options.map((option) => (
              <MenuItem key={option} value={option}>
                {option}
              </MenuItem>
            ))}
          </TextField>
        );
      
      case 'checkbox':
        return (
          <FormControl key={field.name} fullWidth margin="normal" required={field.required}>
            <Typography variant="subtitle1">{field.label}</Typography>
            {field.options.map((option) => (
              <FormControlLabel
                key={option}
                control={
                  <Checkbox
                    checked={formData[section][field.name]?.includes(option) || false}
                    onChange={(e) => handleCheckboxChange(section, field.name, option, e.target.checked)}
                  />
                }
                label={option}
              />
            ))}
          </FormControl>
        );
      
      case 'radio':
        return (
          <FormControl key={field.name} fullWidth margin="normal" required={field.required}>
            <Typography variant="subtitle1">{field.label}</Typography>
            <RadioGroup
              value={value}
              onChange={(e) => handleInputChange(section, field.name, e.target.value)}
            >
              {field.options.map((option) => (
                <FormControlLabel key={option} value={option} control={<Radio />} label={option} />
              ))}
            </RadioGroup>
          </FormControl>
        );
      
      default:
        return null;
    }
  };

  // Render step content
  const getStepContent = (step) => {
    switch (step) {
      case 0:
        return (
          <>
            {!selectedCategory ? (
              <>
                <Typography variant="h6" gutterBottom>
                  Dilekçe Kategorisi Seçin
                </Typography>
                <Grid container spacing={3}>
                  {categories.map((category) => (
                    <Grid item xs={12} sm={6} md={4} key={category.id}>
                      <CategoryCard onClick={() => handleCategorySelect(category)}>
                        <CardContent>
                          <Box display="flex" alignItems="center" mb={2}>
                            {category.icon}
                            <Typography variant="h6" component="h2" ml={1}>
                              {category.name}
                            </Typography>
                          </Box>
                          <Typography variant="body2" color="text.secondary">
                            {category.name} ile ilgili dilekçe şablonlarını görüntüleyin.
                          </Typography>
                        </CardContent>
                      </CategoryCard>
                    </Grid>
                  ))}
                </Grid>
              </>
            ) : (
              <>
                <Box display="flex" alignItems="center" mb={2}>
                  <Button 
                    startIcon={<ArrowBackIcon />} 
                    onClick={() => setSelectedCategory(null)}
                    sx={{ mr: 2 }}
                  >
                    Geri
                  </Button>
                  <Typography variant="h6">
                    {selectedCategory.name} Dilekçeleri
                  </Typography>
                </Box>
                
                {loading ? (
                  <Box display="flex" justifyContent="center" my={4}>
                    <CircularProgress />
                  </Box>
                ) : error ? (
                  <Alert severity="error" sx={{ my: 2 }}>{error}</Alert>
                ) : (
                  <Grid container spacing={3}>
                    {templates.map((template) => (
                      <Grid item xs={12} sm={6} md={4} key={template.id}>
                        <TemplateCard onClick={() => handleTemplateSelect(template)}>
                          <CardContent>
                            <Typography variant="h6" component="h2" gutterBottom>
                              {template.name}
                            </Typography>
                            <Typography variant="body2" color="text.secondary" paragraph>
                              {template.description}
                            </Typography>
                          </CardContent>
                          <CardActions>
                            <Button 
                              size="small" 
                              startIcon={<DescriptionIcon />}
                              onClick={() => handleTemplateSelect(template)}
                            >
                              Seç
                            </Button>
                          </CardActions>
                        </TemplateCard>
                      </Grid>
                    ))}
                  </Grid>
                )}
              </>
            )}
          </>
        );
      
      case 1:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Kişisel Bilgiler
            </Typography>
            
            <Box mb={4}>
              <Typography variant="subtitle1" gutterBottom fontWeight="bold">
                Dilekçe Sahibi Bilgileri
              </Typography>
              {selectedTemplate?.fields
                .filter(field => ['ad_soyad', 'tc_kimlik', 'adres', 'telefon', 'eposta'].includes(field.name))
                .map(field => renderFormField(field, 'userData'))}
            </Box>
            
            <Box>
              <Typography variant="subtitle1" gutterBottom fontWeight="bold">
                Muhatap Bilgileri
              </Typography>
              {selectedTemplate?.fields
                .filter(field => field.name.startsWith('muhatap_'))
                .map(field => renderFormField(field, 'recipientData'))}
            </Box>
          </>
        );
      
      case 2:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Dilekçe İçeriği
            </Typography>
            
            {selectedTemplate?.fields
              .filter(field => !['ad_soyad', 'tc_kimlik', 'adres', 'telefon', 'eposta'].includes(field.name) && 
                              !field.name.startsWith('muhatap_'))
              .map(field => renderFormField(field, 'contentData'))}
          </>
        );
      
      case 3:
        return (
          <>
            <Typography variant="h6" gutterBottom>
              Önizleme ve İndirme
            </Typography>
            
            {loading ? (
              <Box display="flex" justifyContent="center" my={4}>
                <CircularProgress />
              </Box>
            ) : error ? (
              <Alert severity="error" sx={{ my: 2 }}>{error}</Alert>
            ) : generatedPetition ? (
              <>
                <Box mb={3}>
                  <Typography variant="subtitle1" gutterBottom>
                    Dilekçeniz başarıyla oluşturuldu!
                  </Typography>
                  <Typography variant="body2" color="text.secondary" paragraph>
                    Dilekçenizi aşağıdaki butonlardan indirebilir veya e-posta olarak gönderebilirsiniz.
                  </Typography>
                  
                  <Box display="flex" gap={2} mt={2}>
                    <Button 
                      variant="contained" 
                      color="primary" 
                      startIcon={<DownloadIcon />}
                      onClick={() => downloadPetition('pdf')}
                    >
                      PDF İndir
                    </Button>
                    <Button 
                      variant="outlined" 
                      startIcon={<DownloadIcon />}
                      onClick={() => downloadPetition('docx')}
                    >
                      Word İndir
                    </Button>
                    <Button 
                      variant="outlined" 
                      startIcon={<EmailIcon />}
                    >
                      E-posta Gönder
                    </Button>
                  </Box>
                </Box>
                
                <Typography variant="subtitle1" gutterBottom>
                  Dilekçe Önizleme
                </Typography>
                <PreviewContainer>
                  <iframe 
                    src={`${API_URL}/download/${generatedPetition.id}?format=pdf`}
                    width="100%" 
                    height="600px" 
                    title="Dilekçe Önizleme"
                    style={{ border: 'none' }}
                  />
                </PreviewContainer>
              </>
            ) : (
              <Alert severity="info">Dilekçe oluşturuluyor...</Alert>
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
          Dilekçe Üretici
        </Typography>
        <Typography variant="subtitle1" align="center" color="text.secondary" paragraph>
          Hızlı ve kolay bir şekilde profesyonel dilekçeler oluşturun
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
                Yeni Dilekçe Oluştur
              </Button>
            ) : (
              <Button
                variant="contained"
                color="primary"
                onClick={handleNext}
                disabled={(activeStep === 0 && !selectedTemplate) || loading}
              >
                {activeStep === steps.length - 2 ? 'Dilekçe Oluştur' : 'Devam Et'}
              </Button>
            )}
          </Box>
        </Box>
      </StyledPaper>
    </Container>
  );
};

// Missing icons
const HomeIcon = () => <span role="img" aria-label="home">🏠</span>;
const FamilyIcon = () => <span role="img" aria-label="family">👪</span>;
const GavelIcon = () => <span role="img" aria-label="gavel">⚖️</span>;
const MoreIcon = () => <span role="img" aria-label="more">📄</span>;
const ArrowBackIcon = () => <span role="img" aria-label="back">⬅️</span>;
const EmailIcon = () => <span role="img" aria-label="email">📧</span>;

export default PetitionGenerator;
