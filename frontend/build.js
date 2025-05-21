const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Build dizini oluştur
const buildDir = path.join(__dirname, 'build');
if (!fs.existsSync(buildDir)) {
  fs.mkdirSync(buildDir);
}

// HTML dosyası oluştur
const htmlContent = `
<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Türkiye Hukuk AI Platformu</title>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap" />
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="bundle.js"></script>
</body>
</html>
`;

fs.writeFileSync(path.join(buildDir, 'index.html'), htmlContent);

// CSS dosyası oluştur
const cssContent = `
body {
  margin: 0;
  padding: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #f5f5f5;
}

#root {
  min-height: 100vh;
}
`;

fs.writeFileSync(path.join(buildDir, 'styles.css'), cssContent);

// Webpack yapılandırması oluştur
const webpackConfig = `
const path = require('path');

module.exports = {
  mode: 'production',
  entry: './src/index.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'build'),
  },
  module: {
    rules: [
      {
        test: /\\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  },
  resolve: {
    extensions: ['.js', '.jsx']
  },
  optimization: {
    minimize: true
  }
};
`;

fs.writeFileSync(path.join(__dirname, 'webpack.config.js'), webpackConfig);

// package.json güncelle
const packageJson = require('./package.json');
packageJson.scripts = {
  ...packageJson.scripts,
  build: 'webpack --config webpack.config.js'
};

fs.writeFileSync(path.join(__dirname, 'package.json'), JSON.stringify(packageJson, null, 2));

console.log('Frontend build yapılandırması tamamlandı.');
