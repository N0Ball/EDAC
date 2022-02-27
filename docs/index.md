# EDAC
A Learning Program for Error Decoding and Correction

# Test Platform

## NOISE

### Basic Usage

```python
noise_generator = NoiseFactory(NoiseType, debug)
noise_msg = noise_generator.add_noise(MSG)
```

- Sample Usage

```python
noise_generator = NoiseFactory(NoiseType.NO_NOISE, debug=TRUE)
noise_msg = noise_generator.add_noise(b"OUO")
```