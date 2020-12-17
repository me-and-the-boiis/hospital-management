$('table').on('click', '.delete-item', function() {
  $(this).closest('tr').remove()
})

$('.table > tbody').on('click', '.add-item', function() {
  const innerHTML = `
  <tr>
    <td><strong>1</strong></td>
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
        <button class="button is-danger is-inverted">
            <i class="fas fa-minus"></i>
        </button>
    </td>
  </tr>
  `
  $this.append(innerHTML)
})
