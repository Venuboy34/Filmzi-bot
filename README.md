<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>HD Pro Search Bot</title>
  <style>
    body {
      background: #000;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .typing {
      font-family: 'Courier New', monospace;
      font-size: 32px;
      white-space: nowrap;
      overflow: hidden;
      border-right: 4px solid #fff;
      width: 0;
      animation: typing 4s steps(30, end) forwards, blink 0.75s step-end infinite, rainbow 4s linear infinite;
    }

    @keyframes typing {
      from { width: 0; }
      to { width: 100%; }
    }

    @keyframes blink {
      50% { border-color: transparent; }
    }

    @keyframes rainbow {
      0%   { color: #ff0000; }
      14%  { color: #ff9900; }
      28%  { color: #ffff00; }
      42%  { color: #33cc33; }
      57%  { color: #3399ff; }
      71%  { color: #9900cc; }
      85%  { color: #ff3399; }
      100% { color: #ff0000; }
    }
  </style>
</head>
<body>
  <div class="typing">Welcome To HD Pro Search Bot!</div>
</body>
</html>
