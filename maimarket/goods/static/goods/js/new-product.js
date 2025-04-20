
const photoInnerEl = document.querySelector('.photo-preview-wrapper')

fileInput.addEventListener('change', () => {
    const newDiv = document.createElement('div')
    newDiv.classList.add('photo-preview-box')
    const newImgFile = document.createElement('img')
    newImgFile.classList.add('preview__image')

    const deletePhotoElement = document.createElement('button')
    deletePhotoElement.classList.add('delete__photoBTN')
    deletePhotoElement.type = 'button'
    const spanElementFirst = document.createElement('span')

    spanElementFirst.classList.add('red_line')

    const spanElementSecond = document.createElement('span')

    spanElementSecond.classList.add('red_line')


  const file = fileInput.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = e => {
    newImgFile.src = e.target.result;
  };
  reader.readAsDataURL(file);
  deletePhotoElement.append(spanElementFirst, spanElementSecond)
  photoInnerEl.append(newDiv)
  newDiv.append(newImgFile, deletePhotoElement)
});



// Кнопка удаления фотографии из списка

const deletPhotoBtn = document.querySelector(".delete__photoBTN")

document.addEventListener('click', (event)=>{
    if(event.target.classList.contains('delete__photoBTN')){
        const delPhotoELement = event.target.closest('.photo-preview-box')
        delPhotoELement.remove()
    }
    
})










// const input = document.getElementById('price');

// input.addEventListener('input', () => {
//   let val = input.value.replace(/[^\d]/g, ''); // Удаляем всё кроме цифр
//   if (val) {
//     input.value = `${val} ₽`;
//   } else {
//     input.value = ''; // Не показываем ₽ при пустом поле
//   }
// });

// // Чтобы при фокусе можно было редактировать только цифры
// input.addEventListener('focus', () => {
//   input.value = input.value.replace(/[^\d]/g, '');
// });

// // При потере фокуса — снова добавляем ₽
// input.addEventListener('blur', () => {
//   if (input.value) {
//     let bbasd = input.value.split(' ')

//     const [first, second] = bbasd


//     input.value = `${first} ₽` ;
//   }
// });







const input = document.getElementById('price');

input.addEventListener('input', () => {
  let val = input.value.replace(/[^\d]/g, ''); // Удаляем всё кроме цифр
  if (val) {
    input.value = `${val}`;
  } else {
    input.value = ''; // Не показываем ₽ при пустом поле
  }
});
