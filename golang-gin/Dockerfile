# Use the official Golang image to build the application
FROM golang:1.24.0 AS builder

# Set the working directory inside the container
WORKDIR /app

# Copy go.mod and go.sum files to the container
COPY go.mod go.sum ./

# Download all dependencies
RUN go mod download

# Copy the rest of the application source code to the container
COPY . .

# Build the Go application
RUN go build -o gin-server .

# Use a minimal base image for the runtime
FROM debian:bookworm-slim

# Set the working directory
WORKDIR /app

# Copy the built binary from the builder stage
COPY --from=builder /app/gin-server .

# Expose the port the server runs on
EXPOSE 8080

# Run the binary
CMD ["./gin-server"]
