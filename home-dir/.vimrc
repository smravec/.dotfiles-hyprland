call plug#begin()
Plug 'scrooloose/nerdtree'
Plug 'rakr/vim-one' 
Plug 'nickeb96/fish.vim'
Plug 'elkowar/yuck.vim'
call plug#end()

nnoremap <silent> <C-b> :NERDTreeToggle<CR>
vnoremap <silent> <C-y> "yy <Bar> :call system('wl-copy', @y)<CR>

let g:NERDTreeShowHidden = 1
let g:NERDTreeMinimalUI = 1
let g:NERDTreeIgnore = []
let g:NERDTreeStatusline = ''

set number
set shiftwidth=4
set smarttab

set background=dark
colorscheme one
let g:airline_theme='one'

hi Normal guibg=NONE ctermbg=NONE
hi LineNr guibg=NONE ctermbg=NONE
hi SignColumn guibg=NONE ctermbg=NONE
hi EndOfBuffer guibg=NONE ctermbg=NONE
hi Visual cterm=none ctermbg=darkgrey ctermfg=white
