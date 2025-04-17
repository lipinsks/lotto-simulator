document.querySelector('#draw-btn').addEventListener('click', () => {
  fetch('/api/draw')
    .then(res => res.json())
    .then(data => {
      const container = document.querySelector('#balls');
      container.innerHTML = '';
      data.numbers.forEach(num => {
        const ball = document.createElement('div');
        ball.className = 'ball';
        ball.textContent = num;
        container.appendChild(ball);
      });
    });
});

