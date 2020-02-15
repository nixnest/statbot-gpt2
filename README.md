# Statbot GPT2

Uses GPT-2 to train a model on message data. Requires Python >= 3.6.

Data is *not* provided.

## Processing JSON

Message data comes in a specific format from statbot database dumps. Time is in ms.

```
 "columns": [
    "time",
    "authorID",
    "authorName",
    "channelID",
    "channelName",
    "messageText"
  ],
```

Messages can be accessed in the JSON at `.results[0].series[0].values, values`.

If you have a JSON dump, stick it in the `data` folder and then run 
```
python nixnest_gpt2/process.py <channel>`
```

eg 

```
python nixnest_gpt2/process.py dev-urandom
```

## Training

Values for training can be tweaked inside the script. By default it uses:

- 50,000 steps. This should be enough to get a very solid model out of a couple of hundred thousand messages.
    - You can set this to -1 to have training go on indefinitely.
- The 355M model. At the time of writing this is the largest model that can be used for training/generating in this form.

Training can be started with:

```
python nixnest_gpt2/train.py <channel>
```

Restarting the process will cause training to continue from where it was.

Tensorflow 1 (**not 2**) is required. You also require exactly CUDA 10.0.

The trained model should end up in `./checkpoints/run1`.