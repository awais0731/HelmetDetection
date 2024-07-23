from Helmet.pipeline.train_pipeline import TrainPipeline

if __name__ == "__main__":
    # current_time = datetime.now()
    # formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    # print(formatted_time)
    pipeline = TrainPipeline()
    pipeline.run_pipeline()   