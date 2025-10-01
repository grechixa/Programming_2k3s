def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test Example 1
print("Example 1:")
nums1 = [2,7,11,15]
target1 = 9
result1 = twoSum(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}")
print(f"Output: {result1}")
print(f"Expected: [0,1]")
print(f"Test 1: {'PASS' if sorted(result1) == [0,1] else 'FAIL'}")
print(f"Verification: nums[{result1[0]}] + nums[{result1[1]}] = {nums1[result1[0]]} + {nums1[result1[1]]} = {nums1[result1[0]] + nums1[result1[1]]}")
print()

# Test Example 2
print("Example 2:")
nums2 = [3,2,4]
target2 = 6
result2 = twoSum(nums2, target2)
print(f"Input: nums = {nums2}, target = {target2}")
print(f"Output: {result2}")
print(f"Expected: [1,2]")
print(f"Test 2: {'PASS' if sorted(result2) == [1,2] else 'FAIL'}")
print(f"Verification: nums[{result2[0]}] + nums[{result2[1]}] = {nums2[result2[0]]} + {nums2[result2[1]]} = {nums2[result2[0]] + nums2[result2[1]]}")
print()

# Test Example 3
print("Example 3:")
nums3 = [3,3]
target3 = 6
result3 = twoSum(nums3, target3)
print(f"Input: nums = {nums3}, target = {target3}")
print(f"Output: {result3}")
print(f"Expected: [0,1]")
print(f"Test 3: {'PASS' if sorted(result3) == [0,1] else 'FAIL'}")
print(f"Verification: nums[{result3[0]}] + nums[{result3[1]}] = {nums3[result3[0]]} + {nums3[result3[1]]} = {nums3[result3[0]] + nums3[result3[1]]}")
print()

# Summary
print("SUMMARY:")
tests_passed = 0
total_tests = 3

if sorted(result1) == [0,1]: tests_passed += 1
if sorted(result2) == [1,2]: tests_passed += 1
if sorted(result3) == [0,1]: tests_passed += 1

print(f"Tests passed: {tests_passed}/{total_tests}")
print(f"Overall result: {'ALL TESTS PASSED' if tests_passed == total_tests else 'SOME TESTS FAILED'}")