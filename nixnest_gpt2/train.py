import sys
import gpt_2_simple as gpt2
import os.path

model = '355M'
steps = 50000


def train_model(channel: str):
    file_name = 'data/%s.txt' % channel

    if not os.path.exists('model'):
        gpt2.download_gpt2(model_name=model)

    sess = gpt2.start_tf_sess()

    gpt2.finetune(sess,
                  dataset=file_name,
                  model_name=model,
                  steps=steps,
                  restore_from='latest',
                  run_name='run1',
                  print_every=100,
                  sample_every=2000,
                  save_every=500
                  )


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('must specify channel name')
        sys.exit(1)

    train_model(sys.argv[1])

