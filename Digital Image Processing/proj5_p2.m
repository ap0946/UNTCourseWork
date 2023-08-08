%NAME: Alexis Phu

img = imread("DIPcover.bmp");
img = rgb2gray(img);
img = im2double(img);
figure; imshow(img);

img_fft = fft2(img);
mag = abs(img_fft);
phase = angle(img_fft);

spectrum = fftshift(log(1 + abs(img_fft)));
figure; imshow(mat2gray(spectrum));

i_mag = ifft2(mag);
i_mag_img = fftshift(log(1+abs(i_mag)));
figure; imshow(mat2gray(i_mag_img));

phase_0 = exp(1j * phase);
i_phase = ifft2(phase_0);
i_phase_img = log(1+abs(i_phase));
i_phase_img = imadjust(i_phase_img, [], [], 0.5);
figure; imshow(mat2gray(i_phase_img));

img_recon_fft = mag .* exp(1j * phase);
img_recon = ifft2(img_recon_fft);
img_recon_show = log(1+abs(img_recon));
%figure; imshow(mat2gray(img_recon_show));