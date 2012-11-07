module gfunc_interface
    use gfunc_module
    use iso_c_binding
    implicit none
contains
    subroutine c_gfunc(x, n, m, a, b, c) bind(c)
        real(C_DOUBLE), intent(in), value :: x
        integer(C_INT), intent(in), value ::  n, m
        type(C_PTR), intent(in), value :: a, b
        type(C_PTR), value :: c
        
        real(C_DOUBLE), dimension(:), pointer :: fa, fb
        real(C_DOUBLE), dimension(:,:), pointer :: fc
        
        call c_f_pointer(a, fa, (/ n /))
        call c_f_pointer(b, fb, (/ m /))
        call c_f_pointer(c, fc, (/ n, m /))
        call gfunc(x, fa, fb, fc)
    end subroutine

end module
