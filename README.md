<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HD Pro Search Bot</title>
  <style>
    body {
      background-color: #000;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }

    .typing-text {
      font-family: 'Courier New', monospace;
      font-size: 28px;
      white-space: nowrap;
      overflow: hidden;
      border-right: 3px solid #fff;
      animation: typing 4s steps(40, end), blink 0.7s infinite, rainbow 6s linear infinite;
    }

    @keyframes typing {
      from { width: 0 }
      to { width: 100% }
    }

    @keyframes blink {
      50% { border-color: transparent }
    }

    @keyframes rainbow {
      0%   { color: #FF0000; }
      14%  { color: #FFA500; }
      28%  { color: #FFFF00; }
      42%  { color: #00FF00; }
      57%  { color: #00FFFF; }
      71%  { color: #0000FF; }
      85%  { color: #800080; }
      100% { color: #FF0000; }
    }
  </style>
</head>
<body>
  <div class="typing-text">Welcome To HD Pro Search Bot!</div>
</body>
</html>
