from Extractor import LLVM as llvm

module_source = '''source_filename = "functions/sqrt_minus.cpp"
target datalayout = "e-m:o-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-apple-macosx10.12.0"

%"class.std::__1::basic_ostream" = type { i32 (...)**, %"class.std::__1::basic_ios.base" }
%"class.std::__1::basic_ios.base" = type <{ %"class.std::__1::ios_base", %"class.std::__1::basic_ostream"*, i32 }>
%"class.std::__1::ios_base" = type { i32 (...)**, i32, i64, i64, i32, i32, i8*, i8*, void (i32, %"class.std::__1::ios_base"*, i32)**, i32*, i64, i64, i64*, i64, i64, i8**, i64, i64 }
%"class.std::__1::locale::id" = type <{ %"struct.std::__1::once_flag", i32, [4 x i8] }>
%"struct.std::__1::once_flag" = type { i64 }
%"class.std::__1::locale" = type { %"class.std::__1::locale::__imp"* }
%"class.std::__1::locale::__imp" = type opaque
%"class.std::__1::locale::facet" = type { %"class.std::__1::__shared_count" }
%"class.std::__1::__shared_count" = type { i32 (...)**, i64 }
%"class.std::__1::ctype" = type <{ %"class.std::__1::locale::facet", i32*, i8, [7 x i8] }>

@_ZNSt3__14coutE = external global %"class.std::__1::basic_ostream", align 8
@_ZNSt3__15ctypeIcE2idE = external global %"class.std::__1::locale::id", align 8

; Function Attrs: nounwind optsize readnone ssp uwtable
define double @_Z10sqrt_minusd(double) local_unnamed_addr #0 {
  %2 = fcmp olt double %0, 1.000000e+00
  br i1 %2, label %8, label %3

; <label>:3:                                      ; preds = %1
  %4 = tail call double @sqrt(double %0) #6
  %5 = fadd double %0, -1.000000e+00
  %6 = tail call double @sqrt(double %5) #6
  %7 = fsub double %4, %6
  br label %8

; <label>:8:                                      ; preds = %1, %3
  %9 = phi double [ %7, %3 ], [ 0xC1653158E0000000, %1 ]
  ret double %9
}

; Function Attrs: nounwind optsize readnone
declare double @sqrt(double) local_unnamed_addr #1

; Function Attrs: norecurse optsize ssp uwtable
define i32 @main() local_unnamed_addr #2 personality i32 (...)* @__gxx_personality_v0 {
  %1 = alloca %"class.std::__1::locale", align 8
  %2 = bitcast %"class.std::__1::locale"* %1 to i8*
  br label %5

; <label>:3:                                      ; preds = %32
  %4 = call dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd(%"class.std::__1::basic_ostream"* nonnull @_ZNSt3__14coutE, double 0x3FC4C583ADA5B530) #7
  ret i32 0

; <label>:5:                                      ; preds = %0, %32
  %6 = phi i32 [ 0, %0 ], [ %35, %32 ]
  %7 = sitofp i32 %6 to double
  %8 = fmul double %7, 1.000000e-01
  %9 = call dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd(%"class.std::__1::basic_ostream"* nonnull @_ZNSt3__14coutE, double %8) #7
  %10 = bitcast %"class.std::__1::basic_ostream"* %9 to i8**
  %11 = load i8*, i8** %10, align 8, !tbaa !2
  %12 = getelementptr i8, i8* %11, i64 -24
  %13 = bitcast i8* %12 to i64*
  %14 = load i64, i64* %13, align 8
  %15 = bitcast %"class.std::__1::basic_ostream"* %9 to i8*
  %16 = getelementptr inbounds i8, i8* %15, i64 %14
  call void @llvm.lifetime.start(i64 8, i8* %2) #8
  %17 = bitcast i8* %16 to %"class.std::__1::ios_base"*
  call void @_ZNKSt3__18ios_base6getlocEv(%"class.std::__1::locale"* nonnull sret %1, %"class.std::__1::ios_base"* %17) #7
  %18 = invoke %"class.std::__1::locale::facet"* @_ZNKSt3__16locale9use_facetERNS0_2idE(%"class.std::__1::locale"* nonnull %1, %"class.std::__1::locale::id"* nonnull dereferenceable(16) @_ZNSt3__15ctypeIcE2idE) #7
          to label %19 unwind label %26

; <label>:19:                                     ; preds = %5
  %20 = bitcast %"class.std::__1::locale::facet"* %18 to %"class.std::__1::ctype"*
  %21 = bitcast %"class.std::__1::locale::facet"* %18 to i8 (%"class.std::__1::ctype"*, i8)***
  %22 = load i8 (%"class.std::__1::ctype"*, i8)**, i8 (%"class.std::__1::ctype"*, i8)*** %21, align 8, !tbaa !2
  %23 = getelementptr inbounds i8 (%"class.std::__1::ctype"*, i8)*, i8 (%"class.std::__1::ctype"*, i8)** %22, i64 7
  %24 = load i8 (%"class.std::__1::ctype"*, i8)*, i8 (%"class.std::__1::ctype"*, i8)** %23, align 8
  %25 = invoke signext i8 %24(%"class.std::__1::ctype"* %20, i8 signext 10) #7
          to label %32 unwind label %26

; <label>:26:                                     ; preds = %19, %5
  %27 = landingpad { i8*, i32 }
          cleanup
  invoke void @_ZNSt3__16localeD1Ev(%"class.std::__1::locale"* nonnull %1) #7
          to label %28 unwind label %29

; <label>:28:                                     ; preds = %26
  call void @llvm.lifetime.end(i64 8, i8* %2) #8
  resume { i8*, i32 } %27

; <label>:29:                                     ; preds = %26
  %30 = landingpad { i8*, i32 }
          catch i8* null
  %31 = extractvalue { i8*, i32 } %30, 0
  call void @__clang_call_terminate(i8* %31) #9
  unreachable

; <label>:32:                                     ; preds = %19
  call void @_ZNSt3__16localeD1Ev(%"class.std::__1::locale"* nonnull %1) #7
  call void @llvm.lifetime.end(i64 8, i8* %2) #8
  %33 = call dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc(%"class.std::__1::basic_ostream"* nonnull %9, i8 signext %25) #7
  %34 = call dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv(%"class.std::__1::basic_ostream"* nonnull %9) #7
  %35 = add nuw nsw i32 %6, 1
  %36 = icmp slt i32 %35, 10
  br i1 %36, label %5, label %3
}

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.start(i64, i8* nocapture) #3

; Function Attrs: optsize
declare dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEElsEd(%"class.std::__1::basic_ostream"*, double) local_unnamed_addr #4

; Function Attrs: argmemonly nounwind
declare void @llvm.lifetime.end(i64, i8* nocapture) #3

; Function Attrs: optsize
declare dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE3putEc(%"class.std::__1::basic_ostream"*, i8 signext) local_unnamed_addr #4

; Function Attrs: optsize
declare dereferenceable(160) %"class.std::__1::basic_ostream"* @_ZNSt3__113basic_ostreamIcNS_11char_traitsIcEEE5flushEv(%"class.std::__1::basic_ostream"*) local_unnamed_addr #4

; Function Attrs: optsize
declare void @_ZNKSt3__18ios_base6getlocEv(%"class.std::__1::locale"* sret, %"class.std::__1::ios_base"*) local_unnamed_addr #4

declare i32 @__gxx_personality_v0(...)

; Function Attrs: optsize
declare void @_ZNSt3__16localeD1Ev(%"class.std::__1::locale"*) unnamed_addr #4

; Function Attrs: noinline noreturn nounwind
define linkonce_odr hidden void @__clang_call_terminate(i8*) local_unnamed_addr #5 {
  %2 = tail call i8* @__cxa_begin_catch(i8* %0) #8
  tail call void @_ZSt9terminatev() #9
  unreachable
}

declare i8* @__cxa_begin_catch(i8*) local_unnamed_addr

declare void @_ZSt9terminatev() local_unnamed_addr

; Function Attrs: optsize
declare %"class.std::__1::locale::facet"* @_ZNKSt3__16locale9use_facetERNS0_2idE(%"class.std::__1::locale"*, %"class.std::__1::locale::id"* dereferenceable(16)) local_unnamed_addr #4

attributes #0 = { nounwind optsize readnone ssp uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #1 = { nounwind optsize readnone "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #2 = { norecurse optsize ssp uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #3 = { argmemonly nounwind }
attributes #4 = { optsize "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "less-precise-fpmad"="false" "no-frame-pointer-elim"="true" "no-frame-pointer-elim-non-leaf" "no-infs-fp-math"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "stack-protector-buffer-size"="8" "target-cpu"="penryn" "target-features"="+cx16,+fxsr,+mmx,+sse,+sse2,+sse3,+sse4.1,+ssse3,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }
attributes #5 = { noinline noreturn nounwind }
attributes #6 = { nounwind optsize readnone }
attributes #7 = { optsize }
attributes #8 = { nounwind }
attributes #9 = { noreturn nounwind }

!llvm.module.flags = !{!0}
!llvm.ident = !{!1}

!0 = !{i32 1, !"PIC Level", i32 2}
!1 = !{!"Apple LLVM version 8.1.0 (clang-802.0.42)"}
!2 = !{!3, !3, i64 0}
!3 = !{!"vtable pointer", !4, i64 0}
!4 = !{!"Simple C++ TBAA"}
'''


def load_module(ir):
    context = llvm.get_global_context()
    buffer = llvm.create_memory_buffer_with_memory_range_copy(ir,
                                                              len(ir),
                                                              'functions/sqrt_minus')
    return context.parse_ir(buffer)


def get_function_number(ir):
    module = load_module(ir)
    return len(list(module.iter_functions()))


def get_non_existing_basic_block(ir):
    module = load_module(ir)
    first_function = list(module.iter_functions())[0]
    first_basic_block = list(first_function.iter_basic_blocks())[0]
    first_basic_block.get_next().first_instruction()


module = load_module(module_source)
print(get_function_number(module_source))
for func in module.iter_functions():
    func.dump()
    for bb in func.iter_basic_blocks():
        for ins in bb.iter_instructions():
            ins.dump()
