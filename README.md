## DALLE2 Video (wip)

** only to be built after DALLE2 image is done and replicated, and the importance of the prior network is validated **

Direct application of <a href="https://openai.com/dall-e-2/">DALLE-2</a> to video synthesis, using factored space-time <a href="https://github.com/lucidrains/video-diffusion-pytorch">UNet</a> and <a href="https://github.com/lucidrains/TimeSformer-pytorch">Transformers</a>

CLIP could have two approaches. (1) design 3D CLIP using TimesFormer for the video encoding (2) use 2D CLIP with attention pooling at the end

For all you academics out there emailing me, you are free to publish this idea without citing me at all. I'm just after the world of infinite machine dreams, and I don't really care how we get there.
