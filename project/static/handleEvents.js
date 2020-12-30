const medicineTable = $('#medicine-table')
const medicineBody = $('#medicine-body')

const deleteItem = function() {
  $(this).closest('tr').remove()
  const myBody = medicineTable.find('tbody')
  index = 1
  myBody.find('strong').each(function () {
    this.innerHTML = index++
  })
}

medicineTable.on('click', '.delete-item', deleteItem)

$('#add-item').click(function() {
  const myBody = medicineTable.find('tbody')
  const innerHTML = `
  <tr>
      <td><strong>${myBody.find('tr').length+1}</strong></td>
      <td>
          <div class="control">
              <input class="input" type="text" placeholder="Small input">
          </div>
      </td>
      <td>
          <div class="control">
              <input class="input" type="text" placeholder="Small input">
          </div>
      </td>
      <td>
          <button class="button is-danger is-inverted delete-item">
              <i class="fas fa-minus"></i>
          </button>
      </td>
  </tr>
  `
  const item = jQuery.parseHTML(innerHTML);
  $(item).on('click', '.delete-item', deleteItem)
  myBody.append(item)
  medicineBody.scrollTop(medicineBody.height()+9999)
})

function submit() {
  let benh_chuan_doan = $('#benh-chuan-doan').val()

}

// console.log(session['loggedin']);
// if (1) {
//   $('.log-in').style.display = 'none';
// } else {
//   $('.log-out').style.display = 'none';
// }
