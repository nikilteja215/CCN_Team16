# Team16 - Wav2Lip: Precision Lip-syncing for Real-world Videos"

*About*
----------
This repository hosts the code for "A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild". It provides a comprehensive toolkit for generating accurate lip movements from speech in diverse real-world scenarios. With this technology, achieve seamless lip-syncing for any speech input, offering a versatile solution for various applications.

*Highlights*
----------
 - The visual quality discriminator's weights have been recently revised in the readme.
 - Achieve precise lip-syncing in videos to match any target speech with utmost accuracy :100:.
 - Compatible with all identities, voices, and languages, including CGI faces and synthetic voices. :sparkles: .
 - Access comprehensive training code, inference code, and pretrained models :boom:
 - Alternatively, get started quickly using the Google Colab Notebook [Link](https://colab.research.google.com/drive/1VHof_jhHvWlCtIeQNLFBGqJzDqCdJ9U4?usp=sharing).

*Prerequisites*
-------------
- Python 3.6 
- ffmpeg: sudo apt-get install ffmpeg
- Install necessary packages using pip install -r requirements.txt. Alternatively, instructions for using a docker image is provided [here](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668). Have a look at [this comment](https://github.com/Rudrabha/Wav2Lip/issues/131#issuecomment-725478562) and comment on [the gist](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668) if you encounter any issues. 
- Face detection [pre-trained model](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) should be downloaded to face_detection/detection/sfd/s3fd.pth. 

*Getting the weights:*
----------
| Model  | Description |  Link to the model | 
| :-------------: | :---------------: | :---------------: |
| Wav2Lip  | Highly accurate lip-sync | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW)  |
| Wav2Lip + GAN  | Slightly inferior lip-sync, but better visual quality | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EdjI7bZlgApMqsVoEUUXpLsBxqXbn5z8VTmoxp55YNDcIA?e=n9ljGW) |
| Expert Discriminator  | Weights of the expert discriminator | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EQRvmiZg-HRAjvI6zqN9eTEBP74KefynCwPWVmF57l-AYA?e=ZRPHKP) |
| Visual Quality Discriminator  | Weights of the visual disc trained in a GAN setup | [Link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/EQVqH88dTm1HjlK11eNba5gBbn15WMS0B0EZbDBttqrqkg?e=ic0ljo) |

*Easily lip-sync videos with the pre-trained models (Inference)*
-------
You can lip-sync any video to any audio 🗣️:
```bash
python inference.py --checkpoint_path <ckpt> --face <video.mp4> --audio <an-audio-source> 
```
- Synchronized video is saved by default in results/result_voice.mp4.
- Options allow specifying output location and other parameters.
- Supported audio sources include *.wav, *.mp3, or even video files, with automatic audio extraction.

#### Tips for better results:
- Experiment with the `--pads` argument for better face detection by adjusting bounding boxes. You might need to increase the bottom padding to include the chin region, e.g., `--pads 0 20 0 0`.
- Use `--nosmooth` to prevent over-smoothing if mouth positions appear dislocated or show duplicate mouths.
- Adjust `--resize_factor` for lower-resolution videos, potentially enhancing results for 720p compared to 1080p.
- For Wav2Lip model without GAN, further parameter tuning may be needed for optimal results, which can sometimes surpass other models.

*Train!*
----------
There are two major steps: 
(i) Train the expert lip-sync discriminator, 
(ii) Train the Wav2Lip model(s).

#### (i) Training the expert discriminator
- You can download [the pre-trained weights](#getting-the-weights) if you want to skip this step. To train it:
```bash
python color_syncnet_train.py --data_root lrs2_preprocessed/ --checkpoint_dir <folder_to_save_checkpoints>
```
#### (ii) Training the Wav2Lip models
- You can either train the model without the additional visual quality discriminator (< 1 day of training) or use the discriminator (~2 days). For the former, run: 
```bash
python wav2lip_train.py --data_root lrs2_preprocessed/ --checkpoint_dir <folder_to_save_checkpoints> --syncnet_checkpoint_path <path_to_expert_disc_checkpoint>
```

To train with the visual quality discriminator, you should run `hq_wav2lip_train.py` instead. The arguments for both files are similar. In both cases, you can resume training as well. Look at `python wav2lip_train.py --help` for more details. You can also set additional less commonly-used hyper-parameters at the bottom of the `hparams.py` file.

*Training on datasets other than LRS2*
------------------------------------
- Adapting the code for training on datasets other than LRS2 may be necessary.
- Achieving satisfactory results with minimal data or single-speaker samples is a complex research challenge we have yet to address.
- Prior to Wav2Lip training, it's essential to train the expert discriminator specifically for your dataset.
- If using a dataset obtained from the internet, synchronization correction is typically required.
- Take into account the FPS (frames per second) of your dataset's videos, as altering this parameter may necessitate significant code adjustments.
- For optimal outcomes, aim for an expert discriminator eval loss of approximately 0.25 and a Wav2Lip eval sync loss of around 0.2.

*Evaluation*
----------
Please check the `evaluation/` folder for the instructions.
