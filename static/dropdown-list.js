function main() {
    const DIVS = document.getElementsByClassName('dropdown-list')

    console.log(DIVS.length)

    for (const DIV of DIVS) {
        const select  = DIV.getElementsByTagName('select' )[0]
        const display = DIV.getElementsByTagName('section')[0]
        select.addEventListener('change', (event) => {
            block = document.createElement('input')

            block.readOnly  = True
            block.type      = 'text'
            block.value     = event.target.value
            block.className = 'dropdown-list-block'

            display.appendChild(block)
        })
    }
}
main()