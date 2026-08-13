
function main() {
    const DIVS = document.getElementsByClassName('dropdown-list')
    const SELECT = []

    console.log(DIVS.length)

    for (const DIV of DIVS) {
        const select  = DIV.getElementsByTagName('select' )[0]
        const display = DIV.getElementsByTagName('section')[0]

        DIV.array   = []
        select.opened = false
        select.div    = DIV

        SELECT.push(select)

        select.addEventListener('click', (event) => {
            event.stopPropagation()
            event.target.opened = !event.target.opened
            const VALUE = event.target.value
            if ((!event.target.opened) && (!event.target.div.array.includes(VALUE)) && VALUE != '') {
                block = document.createElement('input')

                block.readOnly  = true
                block.type      = 'text'
                block.name      = 'qualification'
                block.value     = VALUE
                block.className = 'dropdown-list-block'

                block.style.margin = 20

                block.addEventListener('click', (event) => {
                    event.stopPropagation()
                    display.removeChild(event.target)
                    DIV.array = DIV.array.filter(item => item !== event.target.value)
                    console.log(event.target.value)
                    console.log(DIV.array)
                })

                DIV.array.push(VALUE)

                display.appendChild(block)

                console.log(block)
                console.log(DIV.array)
                console.log(select.opened)
            }
    })}
    document.addEventListener('click', (event) => {
        for (select of SELECT) {
            console.log(select.opened)
            if (select.opened) {
                select.opened = false
                console.log(select.opened)
        }
    }})
}
main()