import React, { useState, useEffect, useRef } from 'react';
import { 
  Container, 
  Typography, 
  Box, 
  Paper, 
  Grid, 
  TextField, 
  Button, 
  List, 
  ListItem, 
  ListItemText, 
  ListItemIcon, 
  Divider, 
  Chip, 
  Card, 
  CardContent, 
  CardActions, 
  IconButton, 
  Avatar, 
  CircularProgress,
  Link,
  Drawer,
  AppBar,
  Toolbar,
  Tabs,
  Tab,
  Menu,
  MenuItem,
  Tooltip
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { 
  Send as SendIcon,
  Person as PersonIcon,
  SmartToy as BotIcon,
  MoreVert as MoreIcon,
  History as HistoryIcon,
  Delete as DeleteIcon,
  Add as AddIcon,
  Calculate as CalculateIcon,
  Description as DescriptionIcon,
  Search as SearchIcon,
  Info as InfoIcon,
  Link as LinkIcon,
  ArrowBack as ArrowBackIcon,
  Category as CategoryIcon,
  QuestionAnswer as QuestionIcon
} from '@mui/icons-material';
import axios from 'axios';

// API URL
const API_URL = 'http://localhost:8002';

// Styled components
const ChatContainer = styled(Paper)(({ theme }) => ({
  height: 'calc(100vh - 200px)',
  display: 'flex',
  flexDirection: 'column',
  overflow: 'hidden',
}));

const MessagesContainer = styled(Box)(({ theme }) => ({
  flexGrow: 1,
  overflow: 'auto',
  padding: theme.spacing(2),
  backgroundColor: theme.palette.background.default,
}));

const MessageBubble = styled(Box)(({ theme, sender }) => ({
  maxWidth: '70%',
  padding: theme.spacing(1.5),
  borderRadius: theme.shape.borderRadius,
  marginBottom: theme.spacing(1.5),
  position: 'relative',
  wordBreak: 'break-word',
  ...(sender === 'user' ? {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.primary.contrastText,
    alignSelf: 'flex-end',
    borderTopRightRadius: 0,
  } : {
    backgroundColor: theme.palette.background.paper,
    borderTopLeftRadius: 0,
    boxShadow: theme.shadows[1],
  }),
}));

const InputContainer = styled(Box)(({ theme }) => ({
  padding: theme.spacing(2),
  borderTop: `1px solid ${theme.palette.divider}`,
  backgroundColor: theme.palette.background.paper,
}));

const SuggestionChip = styled(Chip)(({ theme }) => ({
  margin: theme.spacing(0.5),
  cursor: 'pointer',
}));

const SessionItem = styled(ListItem)(({ theme, active }) => ({
  borderRadius: theme.shape.borderRadius,
  ...(active && {
    backgroundColor: theme.palette.action.selected,
  }),
  '&:hover': {
    backgroundColor: theme.palette.action.hover,
  },
}));

const drawerWidth = 280;

// Main component
const LegalChatbot = () => {
  // State
  const [message, setMessage] = useState('');
  const [chatHistory, setChatHistory] = useState([]);
  const [suggestions, setSuggestions] = useState([]);
  const [relatedTopics, setRelatedTopics] = useState([]);
  const [references, setReferences] = useState([]);
  const [tools, setTools] = useState([]);
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [sessions, setSessions] = useState([]);
  const [drawerOpen, setDrawerOpen] = useState(true);
  const [categories, setCategories] = useState([]);
  const [faqs, setFaqs] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [tabValue, setTabValue] = useState(0);
  const [anchorEl, setAnchorEl] = useState(null);
  const [userId] = useState('user-' + Math.random().toString(36).substr(2, 9)); // Simüle edilmiş kullanıcı ID'si

  const messagesEndRef = useRef(null);

  // Fetch sessions
  useEffect(() => {
    fetchSessions();
    fetchCategories();
  }, []);

  // Scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [chatHistory]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const fetchSessions = async () => {
    try {
      const response = await axios.get(`${API_URL}/sessions/${userId}`);
      setSessions(response.data);
      
      // Eğer aktif bir oturum yoksa ve oturumlar varsa, ilk oturumu seç
      if (!sessionId && response.data.length > 0) {
        setSessionId(response.data[0].id);
        setChatHistory(response.data[0].messages);
      }
    } catch (error) {
      console.error('Error fetching sessions:', error);
    }
  };

  const fetchCategories = async () => {
    try {
      const response = await axios.get(`${API_URL}/categories`);
      setCategories(response.data.categories);
    } catch (error) {
      console.error('Error fetching categories:', error);
    }
  };

  const fetchFaqs = async (categoryId) => {
    try {
      const response = await axios.get(`${API_URL}/faqs/${categoryId}`);
      setFaqs(response.data.faqs);
    } catch (error) {
      console.error('Error fetching FAQs:', error);
    }
  };

  const handleCategorySelect = (category) => {
    setSelectedCategory(category);
    fetchFaqs(category.id);
  };

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleDeleteSession = async () => {
    if (!sessionId) return;
    
    try {
      await axios.delete(`${API_URL}/session/${sessionId}`);
      
      // Oturumu listeden kaldır
      setSessions(sessions.filter(session => session.id !== sessionId));
      
      // Başka bir oturum seç veya yeni oturum oluştur
      if (sessions.length > 1) {
        const newSessionId = sessions.find(session => session.id !== sessionId)?.id;
        if (newSessionId) {
          loadSession(newSessionId);
        } else {
          createNewSession();
        }
      } else {
        createNewSession();
      }
      
      handleMenuClose();
    } catch (error) {
      console.error('Error deleting session:', error);
    }
  };

  const loadSession = async (id) => {
    try {
      const response = await axios.get(`${API_URL}/session/${id}`);
      setSessionId(id);
      setChatHistory(response.data.messages);
      setSuggestions([]);
      setRelatedTopics([]);
      setReferences([]);
      setTools([]);
    } catch (error) {
      console.error('Error loading session:', error);
    }
  };

  const createNewSession = () => {
    setSessionId(null);
    setChatHistory([]);
    setSuggestions([]);
    setRelatedTopics([]);
    setReferences([]);
    setTools([]);
  };

  const handleSendMessage = async () => {
    if (!message.trim()) return;
    
    // Kullanıcı mesajını ekle
    const userMessage = { role: 'user', content: message };
    setChatHistory(prev => [...prev, userMessage]);
    
    // Giriş alanını temizle
    setMessage('');
    
    // Yükleniyor durumunu ayarla
    setLoading(true);
    
    try {
      // API'ye sorgu gönder
      const response = await axios.post(`${API_URL}/query`, {
        query: message,
        session_id: sessionId,
        user_id: userId
      });
      
      // Yanıtı ekle
      const botMessage = { role: 'assistant', content: response.data.response };
      setChatHistory(prev => [...prev, botMessage]);
      
      // Oturum ID'sini güncelle (yeni oturum oluşturulduysa)
      if (!sessionId) {
        setSessionId(response.data.session_id);
      }
      
      // Önerileri, ilgili konuları ve referansları güncelle
      setSuggestions(response.data.suggestions);
      setRelatedTopics(response.data.related_topics);
      setReferences(response.data.references);
      setTools(response.data.tools);
      
      // Oturumları yenile
      fetchSessions();
    } catch (error) {
      console.error('Error sending message:', error);
      
      // Hata mesajı ekle
      const errorMessage = { 
        role: 'assistant', 
        content: 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.' 
      };
      setChatHistory(prev => [...prev, errorMessage]);
    } finally {
      // Yükleniyor durumunu kaldır
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setMessage(suggestion);
    handleSendMessage();
  };

  const handleToolClick = (tool) => {
    // Araç tipine göre işlem yap
    if (tool.type === 'calculator') {
      // Hesaplama aracını aç
      alert(`${tool.name} aracı açılacak`);
    } else if (tool.type === 'petition') {
      // Dilekçe oluşturma aracını aç
      alert(`${tool.name} aracı açılacak`);
    } else if (tool.type === 'contract_analysis') {
      // Sözleşme analizi aracını aç
      alert(`${tool.name} aracı açılacak`);
    }
  };

  const handleFaqClick = (question) => {
    setMessage(question);
    handleSendMessage();
  };

  const toggleDrawer = () => {
    setDrawerOpen(!drawerOpen);
  };

  return (
    <Box sx={{ display: 'flex', height: '100vh' }}>
      {/* Yan Panel */}
      <Drawer
        variant="persistent"
        anchor="left"
        open={drawerOpen}
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
          },
        }}
      >
        <Toolbar />
        <Box sx={{ overflow: 'auto', p: 2 }}>
          <Box display="flex" justifyContent="space-between" alignItems="center" mb={2}>
            <Typography variant="h6">Sohbetler</Typography>
            <Button
              variant="contained"
              size="small"
              startIcon={<AddIcon />}
              onClick={createNewSession}
            >
              Yeni
            </Button>
          </Box>
          
          <List>
            {sessions.map((session) => (
              <SessionItem
                key={session.id}
                active={session.id === sessionId}
                onClick={() => loadSession(session.id)}
                secondaryAction={
                  session.id === sessionId && (
                    <IconButton edge="end" onClick={handleMenuClick}>
                      <MoreIcon />
                    </IconButton>
                  )
                }
              >
                <ListItemIcon>
                  <HistoryIcon />
                </ListItemIcon>
                <ListItemText 
                  primary={session.title} 
                  secondary={new Date(session.updated_at).toLocaleString()}
                />
              </SessionItem>
            ))}
          </List>
          
          <Menu
            anchorEl={anchorEl}
            open={Boolean(anchorEl)}
            onClose={handleMenuClose}
          >
            <MenuItem onClick={handleDeleteSession}>
              <ListItemIcon>
                <DeleteIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText>Sohbeti Sil</ListItemText>
            </MenuItem>
          </Menu>
          
          <Divider sx={{ my: 2 }} />
          
          <Box>
            <Tabs value={tabValue} onChange={handleTabChange}>
              <Tab icon={<CategoryIcon />} label="Kategoriler" />
              <Tab icon={<QuestionIcon />} label="SSS" />
            </Tabs>
            
            {tabValue === 0 && (
              <List>
                {categories.map((category) => (
                  <ListItem 
                    key={category.id} 
                    button
                    selected={selectedCategory?.id === category.id}
                    onClick={() => handleCategorySelect(category)}
                  >
                    <ListItemText primary={category.name} />
                  </ListItem>
                ))}
              </List>
            )}
            
            {tabValue === 1 && (
              <List>
                {faqs.map((faq, index) => (
                  <ListItem 
                    key={index} 
                    button
                    onClick={() => handleFaqClick(faq.question)}
                  >
                    <ListItemText 
                      primary={faq.question} 
                      primaryTypographyProps={{ variant: 'body2' }}
                    />
                  </ListItem>
                ))}
              </List>
            )}
          </Box>
        </Box>
      </Drawer>
      
      {/* Ana İçerik */}
      <Box
        component="main"
        sx={{
          flexGrow: 1,
          p: 3,
          width: { sm: `calc(100% - ${drawerWidth}px)` },
          ml: { sm: `${drawerWidth}px` },
        }}
      >
        <AppBar 
          position="fixed" 
          sx={{ 
            width: { sm: `calc(100% - ${drawerWidth}px)` },
            ml: { sm: `${drawerWidth}px` },
          }}
        >
          <Toolbar>
            <IconButton
              color="inherit"
              edge="start"
              onClick={toggleDrawer}
              sx={{ mr: 2, display: { sm: 'none' } }}
            >
              <ArrowBackIcon />
            </IconButton>
            <Typography variant="h6" noWrap component="div">
              Hukuki Chatbot
            </Typography>
          </Toolbar>
        </AppBar>
        <Toolbar />
        
        <ChatContainer>
          <MessagesContainer>
            {chatHistory.length === 0 ? (
              <Box 
                display="flex" 
                flexDirection="column" 
                alignItems="center" 
                justifyContent="center" 
                height="100%"
              >
                <BotIcon sx={{ fontSize: 80, color: 'text.secondary', mb: 2 }} />
                <Typography variant="h5" color="text.secondary" gutterBottom>
                  Hukuki Asistanınız
                </Typography>
                <Typography variant="body1" color="text.secondary" align="center">
                  Hukuki sorularınızı yanıtlamak için buradayım. Aşağıdaki önerilerden birini seçebilir veya kendi sorunuzu yazabilirsiniz.
                </Typography>
                <Box mt={4} display="flex" flexWrap="wrap" justifyContent="center">
                  <SuggestionChip 
                    label="İşten çıkarıldım, haklarım nelerdir?" 
                    onClick={() => handleSuggestionClick("İşten çıkarıldım, haklarım nelerdir?")}
                  />
                  <SuggestionChip 
                    label="Kira artış oranı ne kadar olabilir?" 
                    onClick={() => handleSuggestionClick("Kira artış oranı ne kadar olabilir?")}
                  />
                  <SuggestionChip 
                    label="Ayıplı mal iade süresi nedir?" 
                    onClick={() => handleSuggestionClick("Ayıplı mal iade süresi nedir?")}
                  />
                </Box>
              </Box>
            ) : (
              <>
                {chatHistory.map((msg, index) => (
                  <Box
                    key={index}
                    sx={{
                      display: 'flex',
                      flexDirection: 'column',
                      alignItems: msg.role === 'user' ? 'flex-end' : 'flex-start',
                    }}
                  >
                    <Box display="flex" alignItems="center" mb={0.5}>
                      {msg.role === 'assistant' ? (
                        <Avatar sx={{ bgcolor: 'primary.main', width: 28, height: 28, mr: 1 }}>
                          <BotIcon fontSize="small" />
                        </Avatar>
                      ) : (
                        <Avatar sx={{ bgcolor: 'secondary.main', width: 28, height: 28, mr: 1 }}>
                          <PersonIcon fontSize="small" />
                        </Avatar>
                      )}
                      <Typography variant="caption" color="text.secondary">
                        {msg.role === 'user' ? 'Siz' : 'Hukuk AI'}
                      </Typography>
                    </Box>
                    <MessageBubble sender={msg.role}>
                      <Typography variant="body1">
                        {msg.content}
                      </Typography>
                    </MessageBubble>
                  </Box>
                ))}
                <div ref={messagesEndRef} />
              </>
            )}
          </MessagesContainer>
          
          {/* Öneriler, İlgili Konular ve Araçlar */}
          {(suggestions.length > 0 || relatedTopics.length > 0 || tools.length > 0) && (
            <Box p={2} bgcolor="background.paper" borderTop={1} borderColor="divider">
              {suggestions.length > 0 && (
                <Box mb={1}>
                  <Typography variant="subtitle2" gutterBottom>
                    Önerilen Sorular:
                  </Typography>
                  <Box display="flex" flexWrap="wrap">
                    {suggestions.map((suggestion, index) => (
                      <SuggestionChip
                        key={index}
                        label={suggestion}
                        onClick={() => handleSuggestionClick(suggestion)}
                        size="small"
                      />
                    ))}
                  </Box>
                </Box>
              )}
              
              {relatedTopics.length > 0 && (
                <Box mb={1}>
                  <Typography variant="subtitle2" gutterBottom>
                    İlgili Konular:
                  </Typography>
                  <Box display="flex" flexWrap="wrap">
                    {relatedTopics.map((topic, index) => (
                      <SuggestionChip
                        key={index}
                        label={topic}
                        onClick={() => handleSuggestionClick(`${topic} hakkında bilgi verir misin?`)}
                        size="small"
                        variant="outlined"
                      />
                    ))}
                  </Box>
                </Box>
              )}
              
              {tools.length > 0 && (
                <Box>
                  <Typography variant="subtitle2" gutterBottom>
                    Kullanabileceğiniz Araçlar:
                  </Typography>
                  <Box display="flex" flexWrap="wrap" gap={1}>
                    {tools.map((tool, index) => (
                      <Button
                        key={index}
                        variant="outlined"
                        size="small"
                        onClick={() => handleToolClick(tool)}
                        startIcon={
                          tool.type === 'calculator' ? <CalculateIcon /> :
                          tool.type === 'petition' ? <DescriptionIcon /> :
                          <SearchIcon />
                        }
                      >
                        {tool.name}
                      </Button>
                    ))}
                  </Box>
                </Box>
              )}
            </Box>
          )}
          
          {/* Referanslar */}
          {references.length > 0 && (
            <Box p={2} bgcolor="background.paper" borderTop={1} borderColor="divider">
              <Typography variant="subtitle2" gutterBottom>
                Yasal Referanslar:
              </Typography>
              <Box display="flex" flexWrap="wrap" gap={1}>
                {references.map((reference, index) => (
                  <Chip
                    key={index}
                    label={reference.title}
                    icon={<LinkIcon />}
                    component={Link}
                    href={reference.url}
                    target="_blank"
                    clickable
                    size="small"
                    variant="outlined"
                  />
                ))}
              </Box>
            </Box>
          )}
          
          {/* Mesaj Giriş Alanı */}
          <InputContainer>
            <Grid container spacing={2}>
              <Grid item xs>
                <TextField
                  fullWidth
                  placeholder="Hukuki sorunuzu yazın..."
                  variant="outlined"
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  onKeyPress={handleKeyPress}
                  disabled={loading}
                  multiline
                  maxRows={4}
                />
              </Grid>
              <Grid item>
                <Button
                  variant="contained"
                  color="primary"
                  endIcon={loading ? <CircularProgress size={20} /> : <SendIcon />}
                  onClick={handleSendMessage}
                  disabled={!message.trim() || loading}
                  sx={{ height: '100%' }}
                >
                  Gönder
                </Button>
              </Grid>
            </Grid>
          </InputContainer>
        </ChatContainer>
      </Box>
    </Box>
  );
};

export default LegalChatbot;
