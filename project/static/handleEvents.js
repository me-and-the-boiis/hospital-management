const medicineTable = $('#medicine-table')
const medicineBody = $('#medicine-body')

medicineTable.on('click', '.delete-item', function() {
  $(this).closest('tr').remove()
  const myBody = medicineTable.find('tbody')
  index = 1
  myBody.find('strong').each(function () {
    this.innerHTML = index++
  })
})

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
  $(item).on('click', '.delete-item', function() {
    $(this).closest('tr').remove()
  })
  myBody.append(item)
  medicineBody.scrollTop(medicineBody.height()+9999)
})
