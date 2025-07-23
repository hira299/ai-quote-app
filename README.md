# AI Quote App

A beautiful, responsive web application that displays inspirational quotes with a modern UI. Built with Next.js frontend and Python serverless backend on AWS Lambda.

## 🌟 Features

- **Random Quote Generator**: 13 inspirational quotes that change randomly
- **Beautiful UI**: Modern, responsive design with smooth animations
- **Serverless Architecture**: Built on AWS Lambda for scalability
- **Real-time Updates**: Click to get new quotes instantly
- **Cross-platform**: Works on desktop and mobile devices

## 🛠️ Tech Stack

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with Flexbox, Grid, and animations
- **JavaScript**: Fetch API, async/await, DOM manipulation

### Backend
- **Python 3.9**: Main programming language
- **AWS Lambda**: Serverless computing platform
- **Serverless Framework**: Deployment and configuration

### Development Tools
- **Node.js 18 LTS**: Runtime environment
- **Python Virtual Environment**: Dependency isolation
- **Serverless Offline**: Local development server

## 📁 Project Structure

```
ai-quote-app/
├── backend/
│   ├── src/
│   │   └── handler.py          # Python Lambda function
│   ├── public/
│   │   └── index.html          # Frontend web page
│   ├── serverless.yml          # Serverless configuration
│   ├── requirements.txt        # Python dependencies
│   └── package.json           # Node.js dependencies
└── README.md
```

## 🚀 Quick Start

### Prerequisites

- Node.js 18 LTS
- Python 3.9
- AWS CLI (for deployment)

### Installation

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd ai-quote-app/backend
```

2. **Install Node.js dependencies:**
```bash
npm install
```

3. **Set up Python virtual environment:**
```bash
python3.9 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

4. **Start the development server:**
```bash
serverless offline
```

5. **Open your browser and visit:**
```
http://localhost:3000
```

## 🎯 Usage

- **View Quotes**: The app displays a random inspirational quote
- **Get New Quote**: Click the "Get New Quote" button to fetch a new random quote
- **Responsive Design**: The app works seamlessly on all device sizes

## 📡 API Endpoints

- `GET /`: Serves the main web page
- `GET /quote`: Returns a random quote in JSON format

### Example API Response:
```json
{
    "quote": "The best way to predict the future is to create it."
}
```

## 🎨 Features

### Frontend
- Gradient background with modern card design
- Hover effects and smooth transitions
- Loading states for better UX
- Error handling with user-friendly messages
- Responsive design for all screen sizes

### Backend
- Serverless architecture for scalability
- CORS support for cross-origin requests
- Error handling and logging
- Random quote selection from 13 inspirational quotes

## 🔧 Configuration

### Environment Variables
- `STAGE`: Deployment stage (default: 'dev')
- `REGION`: AWS region (default: 'us-east-1')

### Serverless Configuration
The `serverless.yml` file contains:
- AWS Lambda function configuration
- API Gateway settings
- CORS configuration
- Plugin settings

## 🚀 Deployment

### Local Development
```bash
serverless offline
```

### AWS Deployment
```bash
serverless deploy
```

## 📝 Available Quotes

The app includes 13 inspirational quotes:
1. "The best way to predict the future is to create it."
2. "Success is not final, failure is not fatal: it is the courage to continue that counts."
3. "Believe you can and you're halfway there."
4. "The only way to do great work is to love what you do."
5. "Innovation distinguishes between a leader and a follower."
6. "The future belongs to those who believe in the beauty of their dreams."
7. "Don't watch the clock; do what it does. Keep going."
8. "The only limit to our realization of tomorrow is our doubts of today."
9. "Everything you've ever wanted is on the other side of fear."
10. "The harder you work for something, the greater you'll feel when you achieve it."
11. "Dream big and dare to fail."
12. "Success is walking from failure to failure with no loss of enthusiasm."
13. "The only person you are destined to become is the person you decide to be."

## 🛠️ Development

### Adding New Quotes
Edit the `QUOTES` list in `backend/src/handler.py`:
```python
QUOTES = [
    "Your new quote here.",
    # ... existing quotes
]
```

### Styling Changes
Modify the CSS in `backend/public/index.html` to customize the appearance.

### API Modifications
Update the `get_quote` function in `backend/src/handler.py` for backend changes.

## 🐛 Troubleshooting

### Common Issues

1. **Node.js Version Error**
   - Ensure you're using Node.js 18: `nvm use 18`

2. **Python Runtime Error**
   - Use Python 3.9: `python3.9 -m venv venv`

3. **Port Already in Use**
   - Check if port 3000 is free: `sudo lsof -i :3000`

4. **CORS Errors**
   - Verify CORS headers are set in the handler

### Error Messages
- **502 Bad Gateway**: Check if the server is running
- **Connection Refused**: Ensure serverless offline is started
- **Module Not Found**: Reinstall dependencies with `npm install`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by motivational quotes
- Built with modern web technologies
- Powered by AWS serverless architecture

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Check the troubleshooting section above
- Review the serverless framework documentation

---

**Made with ❤️ using AI-assisted development** 