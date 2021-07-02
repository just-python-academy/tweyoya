let text = document.getElementById('id_text');
let count = document.getElementById('count');

text.addEventListener('keyup', e => {
  let num = twttr.txt.getTweetLength(e.target.value) / 2;
  count.innerHTML = num;
  num <= 140
    ? count.classList.remove('text-danger')
    : count.classList.add('text-danger');
})

$('#id_tweeted_at').datetimepicker({
  timepicker:true,
  format:'Y-m-d H:i',
});

window.onload = (() => {
  let img = document.getElementById('id_img');
  let mainImage = document.getElementById('mainImage');

  img.addEventListener('change', e => {
    let reader = new FileReader();
    reader.onload = e => {
      mainImage.src = e.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);
  })
})