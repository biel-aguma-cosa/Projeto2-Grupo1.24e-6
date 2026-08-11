function main() {
    const DIVS = document.getElementsByClassName('dropdown-list')

    console.log(DIVS.length)

    for (const DIV of DIVS) {
        const select  = DIV.getElementsByTagName('select' )[0]
        const display = DIV.getElementsByTagName('section')[0]

        DIV.array   = []
        select.opened = false
        select.div    = DIV

        select.addEventListener('click', (event) => {
            event.target.opened = !event.target.opened
            const VALUE = event.target.value
            if ((!event.target.opened) && (!event.target.div.array.includes(VALUE))) {
                block = document.createElement('input')

                block.readOnly  = true
                block.type      = 'text'
                block.name      = 'qualification'
                block.value     = VALUE
                block.className = 'dropdown-list-block'

                DIV.array.push(VALUE)

                display.appendChild(block)

                console.log(block)
                console.log(DIV.array)

                event.target.value = 'add qualification'
            }
        })
    }
}
main()