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
  ListItemAvatar, 
  Avatar, 
  Divider, 
  CircularProgress,
  Card,
  CardContent,
  IconButton,
  Chip
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { 
  Send as SendIcon,
  Person as PersonIcon,
  SmartToy as BotIcon,
  Link as LinkIcon,
  Description as DescriptionIcon,
  Gavel as GavelIcon
} from '@mui/icons-material';
import axios from 'axios';

// API URL
const API_URL = 'http://localhost:8002';

// Styled components
const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(4),
  marginBottom: theme.spacing(3),
}));

const ChatContainer = styled(Box)(({ theme }) => ({
  height: '500px',
  overflowY: 'auto',
  padding: theme.spacing(2),
  backgroundColor: theme.palette.background.default,
  borderRadius: theme.shape.borderRadius,
  border: `1px solid ${theme.palette.divider}`,
}));

const MessageBubble = styled(Box)(({ theme, isUser }) => ({
  backgroundColor: isUser ? theme.palette.primary.light : theme.palette.grey[100],
  color: isUser ? theme.palette.primary.contrastText : theme.palette.text.primary,
  padding: theme.spacing(1.5, 2),
  borderRadius: theme.spacing(2),
  borderTopLeftRadius: isUser ? theme.spacing(2) : theme.spacing(0.5),
  borderTopRightRadius: isUser ? theme.spacing(0.5) : theme.spacing(2),
  maxWidth: '80%',
  marginLeft: isUser ? 'auto' : '0',
  marginRight: isUser ? '0' : 'auto',
  marginBottom: theme.spacing(1),
  wordBreak: 'break-word',
}));

const SuggestionChip = styled(Chip)(({ theme }) => ({
  margin: theme.spacing(0.5),
  cursor: 'pointer',
}));

// Main component
const LegalChatbot = () => {
  // State
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [suggestions, setSuggestions] = useState([]);
  const [relatedTopics, setRelatedTopics] = useState([]);
  const [references, setReferences] = useState([]);
  const [tools, setTools] = useState([]);
  const chatEndRef = useRef(null);

  // Initialize session
  useEffect(() => {
    const storedSessionId = localStorage.getItem('chatSessionId');
    if (storedSessionId) {
      setSessionId(storedSessionId);
      fetchSessionMessages(storedSessionId);
    } else {
      createNewSession();
    }
  }, []);

  // Scroll to bottom when messages change
  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Fetch session messages
  const fetchSessionMessages = async (id) => {
    try {
      const response = await axios.get(`${API_URL}/session/${id}`);
      if (response.data && response.data.messages) {
        setMessages(response.data.messages);
      }
    } catch (error) {
      console.error('Error fetching session messages:', error);
      // If session not found, create a new one
      createNewSession();
    }
  };

  // Create new session
  const createNewSession = async () => {
    try {
      // For simplicity, we'll just generate a random ID
      // In a real app, you would call the API to create a session
      const newSessionId = 'session_' + Math.random().toString(36).substring(2, 15);
      setSessionId(newSessionId);
      localStorage.setItem('chatSessionId', newSessionId);
      setMessages([
        {
          role: 'assistant',
          content: "Merhaba! Ben Türkiye Hukuk AI Platformu'nun hukuki chatbot'uyum. Size nasıl yardımcı olabilirim?",
          timestamp: new Date().toISOString()
        }
      ]);
    } catch (error) {
      console.error('Error creating new session:', error);
    }
  };

  // Send message
  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = {
      role: 'user',
      content: input,
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post(`${API_URL}/chat`, {
        query: input,
        session_id: sessionId
      });

      const assistantMessage = {
        role: 'assistant',
        content: response.data.response,
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, assistantMessage]);
      setSuggestions(response.data.suggestions || []);
      setRelatedTopics(response.data.related_topics || []);
      setReferences(response.data.references || []);
      setTools(response.data.tools || []);
    } catch (error) {
      console.error('Error sending message:', error);
      
      const errorMessage = {
        role: 'assistant',
        content: 'Üzgünüm, bir hata oluştu. Lütfen tekrar deneyin.',
        timestamp: new Date().toISOString()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  // Handle input change
  const handleInputChange = (e) => {
    setInput(e.target.value);
  };

  // Handle key press
  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  };

  // Handle suggestion click
  const handleSuggestionClick = (suggestion) => {
    setInput(suggestion);
    sendMessage();
  };

  // Scroll to bottom of chat
  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // Format timestamp
  const formatTimestamp = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <Container maxWidth="lg">
      <StyledPaper>
        <Typography variant="h4" component="h1" gutterBottom align="center">
          Hukuki Chatbot
        </Typography>
        <Typography variant="body1" paragraph align="center">
          Hukuki sorularınızı sorun, anında yanıt alın.
        </Typography>

        <Grid container spacing={3}>
          <Grid item xs={12} md={8}>
            <ChatContainer>
              {messages.map((message, index) => (
                <Box key={index} sx={{ mb: 2 }}>
                  <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                    <Avatar 
                      sx={{ 
                        bgcolor: message.role === 'user' ? 'primary.main' : 'secondary.main',
                        width: 32,
                        height: 32,
                        mr: 1
                      }}
                    >
                      {message.role === 'user' ? <PersonIcon /> : <BotIcon />}
                    </Avatar>
                    <Typography variant="subtitle2">
                      {message.role === 'user' ? 'Siz' : 'Hukuk AI'}
                    </Typography>
                    <Typography variant="caption" sx={{ ml: 1, color: 'text.secondary' }}>
                      {message.timestamp && formatTimestamp(message.timestamp)}
                    </Typography>
                  </Box>
                  <MessageBubble isUser={message.role === 'user'}>
                    <Typography variant="body1" sx={{ whiteSpace: 'pre-line' }}>
                      {message.content}
                    </Typography>
                  </MessageBubble>
                </Box>
              ))}
              {loading && (
                <Box sx={{ display: 'flex', justifyContent: 'center', my: 2 }}>
                  <CircularProgress size={24} />
                </Box>
              )}
              <div ref={chatEndRef} />
            </ChatContainer>

            <Box sx={{ display: 'flex', mt: 2 }}>
              <TextField
                fullWidth
                variant="outlined"
                placeholder="Hukuki sorunuzu yazın..."
                value={input}
                onChange={handleInputChange}
                onKeyPress={handleKeyPress}
                disabled={loading}
                multiline
                maxRows={3}
              />
              <Button
                variant="contained"
                color="primary"
                endIcon={<SendIcon />}
                onClick={sendMessage}
                disabled={!input.trim() || loading}
                sx={{ ml: 1, minWidth: '120px' }}
              >
                Gönder
              </Button>
            </Box>

            {suggestions.length > 0 && (
              <Box sx={{ mt: 2 }}>
                <Typography variant="subtitle2" gutterBottom>
                  Önerilen Sorular:
                </Typography>
                <Box>
                  {suggestions.map((suggestion, index) => (
                    <SuggestionChip
                      key={index}
                      label={suggestion}
                      onClick={() => handleSuggestionClick(suggestion)}
                      color="primary"
                      variant="outlined"
                    />
                  ))}
                </Box>
              </Box>
            )}
          </Grid>

          <Grid item xs={12} md={4}>
            {relatedTopics.length > 0 && (
              <Card sx={{ mb: 2 }}>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    İlgili Konular
                  </Typography>
                  <List dense>
                    {relatedTopics.map((topic, index) => (
                      <ListItem 
                        key={index}
                        button
                        onClick={() => handleSuggestionClick(`${topic} hakkında bilgi verir misin?`)}
                      >
                        <ListItemText primary={topic} />
                      </ListItem>
                    ))}
                  </List>
                </CardContent>
              </Card>
            )}

            {references.length > 0 && (
              <Card sx={{ mb: 2 }}>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Yasal Referanslar
                  </Typography>
                  <List dense>
                    {references.map((reference, index) => (
                      <ListItem key={index} button component="a" href={reference.url} target="_blank">
                        <ListItemAvatar>
                          <Avatar sx={{ bgcolor: 'primary.main', width: 28, height: 28 }}>
                            <GavelIcon fontSize="small" />
                          </Avatar>
                        </ListItemAvatar>
                        <ListItemText 
                          primary={reference.title} 
                          secondary={reference.description}
                        />
                        <LinkIcon fontSize="small" color="action" />
                      </ListItem>
                    ))}
                  </List>
                </CardContent>
              </Card>
            )}

            {tools.length > 0 && (
              <Card>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    Kullanabileceğiniz Araçlar
                  </Typography>
                  <List dense>
                    {tools.map((tool, index) => (
                      <ListItem key={index} button component="a" href={tool.url}>
                        <ListItemAvatar>
                          <Avatar sx={{ bgcolor: 'secondary.main', width: 28, height: 28 }}>
                            <DescriptionIcon fontSize="small" />
                          </Avatar>
                        </ListItemAvatar>
                        <ListItemText 
                          primary={tool.name} 
                          secondary={tool.description}
                        />
                      </ListItem>
                    ))}
                  </List>
                </CardContent>
              </Card>
            )}

            <Button
              variant="outlined"
              color="primary"
              fullWidth
              onClick={createNewSession}
              sx={{ mt: 2 }}
            >
              Yeni Sohbet Başlat
            </Button>
          </Grid>
        </Grid>
      </StyledPaper>
    </Container>
  );
};

export default LegalChatbot;
