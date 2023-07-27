from PredictionsServer import PredictionsServer

def main():
    server = PredictionsServer('localhost', 8765)
    server.run()

if __name__ == '__main__':
    main()