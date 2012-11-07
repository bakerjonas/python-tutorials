module gfunc_module
    implicit none
contains
    subroutine gfunc(x, a, b, c)
        real(8), intent(in) :: x
        real(8), dimension(:), intent(in) :: a, b
        real(8), dimension(:,:), intent(out) :: c
        
        integer :: i, j, n, m
        n = size(a)
        m = size(b)
        do j=1,m
            do i=1,n
                c(i,j) = exp(-x * (a(i)**2 + b(j)**2))
            end do
        end do
    end subroutine
end module
