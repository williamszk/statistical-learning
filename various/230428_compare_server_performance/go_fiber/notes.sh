go mod init go_fiber_performance_test
go mod tidy

# ==================================================
go build -o main.exe main.go
./main.exe

# ==================================================
go get github.com/gofiber/fiber/v2