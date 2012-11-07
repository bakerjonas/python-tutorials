program main
    use gfunc_module
    implicit none

    integer :: i
    real(8), dimension(100) :: a, b
    real(8), dimension(100, 100), target :: c

    do i=1,100
        a(i) = 0.1 * i
        b(i) = 0.1 * i
    end do
    call gfunc(10.d0, a, b, c)

    do i=1,100
        print *, c(:,i)
    end do
    
end program
