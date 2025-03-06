<!DOCTYPE html>
<html>
<head>
<title>Кнопка</title>
<style>
.button {
  background-image: url('https://i.pinimg.com/736x/0f/81/15/0f81156086a1c3e635fdd7d2ff162945.jpg'e455030ccb961fb2'); /* Первое изображение */
  background-size: contain;
  width: 100px;
  height: 100px;
  border: none;
  cursor: pointer;
}
</style>
</head>
<body>

<button class="button" id="myButton"></button>

<script>
const button = document.getElementById('myButton');
let clickCount = 0;

button.addEventListener('click', () => {
  clickCount++;
  fetch('/click', { // Отправить запрос на сервер
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ count: clickCount }) // Отправить число кликов
  })
  .then(response => response.json())
  .then(data => {
    if (data.image) {
        button.style.backgroundImage = `url(${data.image})`; // Обновить изображение кнопки с сервера
    }
  });
});
</script>

</body>
</html>

